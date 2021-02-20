import re

outputFileName = "output.txt"

def outputPath(lineScope, currentPath, parent):
  startIndex = currentPath.find(parent)
  if(startIndex == -1 or parent == ''):
    return lineScope
  else:
    endIndex = startIndex + len(parent)
    return currentPath[0:endIndex] + "::" + lineScope

currentScope = ""
closestParent = ""

exp = re.compile(r"""
^
\s*
(
(?P<scope>[a-zA-Z]+)(\s\((?P<parent>[a-zA-Z]+)\))*:
|
(?P<listing>[A-Za-z0-9_]+)(?P<isfunction>\([a-z\.,\s]*\))*
(
\s
(
(((?P<isevent>event\s*)|((-\s)(?P<doesreturn>returns\s)*(?P<io>[a-z]+)*(?P<readonly>\s\(read\sonly\))*\s*))*(-\s(?P<description>.*))*)
)$
)*
)
""", re.X) 

text_file = open(outputFileName, "w")
text_file.write('{|class="wikitable sortable plainrowheaders" style="text-align:right"\n|-\n!Category !! Type !! Name !! class="unsortable" | Description (* = From -scriptfunctions) !! Input(I)/Output(O)!! Side !! Permissions\n|-\n')

for line in open("scriptfunctions_client.txt"):
  m = re.match(exp,line)
  if m:
    io = '-'

    if m.group('scope'):
      closestParent = m.group('scope')
      currentScope = outputPath(closestParent, currentScope, m.group('parent') if m.group('parent') else '')

    entryType = "Flag"
    if m.group('isfunction'):
      if m.group('isevent'):
        entryType = 'Event'
      else:
        entryType = 'Function'

    if m.group('doesreturn') or m.group('readonly'):
      io = "O: "
    elif entryType == 'Flag':
      io = "I/O?: "

    if m.group('listing'):
      print(m.group('listing'))
      text_file.write('!' + currentScope + '||'
        + entryType + '||[['
        + closestParent + '::' + m.group('listing') + '|' + m.group('listing') + (m.group('isfunction') if m.group('isfunction') else '') + ']]||'
        + (('*' + m.group('description')) if m.group('description') else '-') + '||'
        + io + (m.group('io') if m.group('io') else '') + '||'
        + 'Unconfirmed||'
        + ( '-' if entryType == 'Function' else ('r' if m.group('readonly') else 'Undetermined'))
        + '\n|-\n')
  
text_file.close()
