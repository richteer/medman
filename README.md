=Medman


Simple usage:
```
./medman <command> <args>
```


Medman is modular, so the available commands depends on the modules you have.
For example, the "list" module will list all registered names.

==Design

The idea behind Medman is simple: provide a way to catalogue media locations and metadata, that is easy to modify with and without this utility.
Furthermore, it intends to be extendable, to allow for new modules (commands) to be added to further simplify the process of storing and retrieving such information.

Medman is just a utility that operates on stored data, which is seperated into the following components (in descending order of abstraction):
 - Directory Tree
 - Categories
 - Names
 - Entries

===Directory Tree
All information in Medman is stored in a directory tree of json files.
The tree itself is are only directories, and in fact, store no data themselves, other than providing the structure and a predictable location of the important files.
Each directory contained in the base directory is a category, and each subdir of those is yet another category.
Categories terminate with a name json file, and each subdirectory in a directory with an associated name are components within that name.

===Categories
Categories seperate media, and are infinitely nestable.
They are intended for more general separation, like Music from Videos.
An example of a nested category would then be separating MP3 from FLAC.
It is not recommended to use for things like genre however, as genres are more specific to a type of media, and some may have more than one genre.

===Names
Names are like a more specific category.
In being more specific, they are also extensible.
Unlike the Directory Tree or Categories, names can store arbitary data about the particular set of media.
This arbitrary data no longer becomes a part of the Medman system, and lies in the hands of the modules.
So, for example, a Name could be a particular TV Show, and genre(s) would then be good use of the arbitrary data stored within.
A list of files is expected under a name, for modules like ``play``.
Names can also specify Entries, which are more specific to a particular file.
In other words, Names are essentially terminal Categories with general metadata.

===Entries
As mentioned in the Names section, Entries are bottom-level, file-specific chunks of metadata.
These are also completely extendable with any specific information about this particular file (read: Entry in the Name).
Continuing the example from the previous section, if the Name is a particular TV Show, an Entry would be a particular episode, and may contain information like Relevant Characters, a synopsis, etc.
Entries may also contain file names as well, and it is expected to agree with the Name's list.
If there is a difference, the Name's file is taken over the Entry's as Entry metadata will almost always be completely managed by additional modules.


=="Managing"
A Medman system only defines a Directory Tree, a set of Categories, and basic interaction with Names.
Everything else is included as a module, either officially supported or not.
Thus, there are very few "required" entries in the descriptor files, which are the following:
 - index.json at the root of the Directory Tree, must contain a list of names, and path (in the Directory Tree) to the Name's dir.
 - Name json files must be named "(Media Name).json", where (Media Name) matches the entry in index.json, and the Name's dir.
 - Name json files must contain an entry "files", with a list of files owned by that Name.
