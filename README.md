# pixies
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
    Derived from putDataInProto.pixie, does nothing more for now.
    

They're all works in progress, the bool type isn't taken into account yet
and some tweaks may be necessary for them to work in ALL cases. They suit
my purpose, no garantee whatsoever that they will suit yours.
