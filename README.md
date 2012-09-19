# node-webvtt

A node.js command line interface and npm package for the WebVTT JavaScript parser.

This is a simple command line wrapper around the WebVTT JavaScript parser. It was written to enable faster development of a WebVTT test suite. Th
e npm module includes the WebVTT parser, and allows one to pass file(s) in order to be validated.

## Installation

    $ npm install webvtt

installs the `webvtt` shell command.

## Examples

Validate a single file, printing error messages, if any:

    $ webvtt file.vtt

Validate two files, printing error messages, if any:

    $ webvtt file1.vtt file2.vtt

Validate a single file, don't print error messages:

    $ webvtt -s file.vtt

## Synopsis

```
$ webvtt
Usage: webvtt [options] <file...>

Options:

  -h, --help     output usage information
  -V, --version  output the version number
  -s, --silent   don't print errors messages
```

## Output

The `webvtt` command will exit with an error code of 0 (no errors) or 1 (errors), depending on the file(s) given as input. If run in silent mode (-s or --silent), no output will be printed, otherwise each error encountered in a file will be printed in the following format:

```
filename:linenumber.column: message
```

For example:

```
$ webvtt file.vtt
file.vtt:1.0: No valid signature. (File needs to start with "WEBVTT".)
```

## Thanks

This project respectfully uses code from and thanks the authors of:

* [webvtt.js](https://bitbucket.org/annevk/webvtt)
* [commander](https://github.com/visionmedia/commander.js)

## License

Copyright (c) 2012, David Humphrey <david.humphrey@senecacollege.ca>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
