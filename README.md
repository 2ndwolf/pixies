# pixies
<pre>
My pixie files

This repository is for me to have backups of my pixie files made with the excellent regexp editor Pixie.
http://www.regexpixie.com/

Since a pixie file is a lot of work and the save feature is lacking. I made a repository.
I will sooner or later add a description for each of my pixie files.

For now:
  putDataInProto.pixie (WIP):
    This one takes a regular cpp header file with classes and a namespace and transforms
    it into code to put data from that files into a google protobuf.
  
  componentTOproto.pixie (WIP):
    Takes the same cpp header file and transforms it into a .proto file. (Further editing neccessary
    to add custom int types and required fields).
    
  marshallComponents.pixie (WIP):
    Derived from putDataInProto.pixie, takes a header file and builds "messages".
    
  GS2Wiki6Nodupes.pixie (see python folder):
    Takes a list (Graal.exe -scripfunctions) and transforms it in a Wiki compatible table. I had to
    make a python out of it to be able to parse the whole file in one go.
    
  headerMaker.pixie (WIP):
    Takes cpp code and makes a header out of it.
    

Some tweaks may be necessary for the regular expressions to work in ALL cases. 
The works in progress aren't to be used without a quick verification. 
These suit my purpose, no garantee whatsoever that they will suit yours.
</pre>
