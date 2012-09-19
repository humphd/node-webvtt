# node-webvtt

A node.js command line interface and npm package for the WebVTT JavaScript parser.

This is a simple command line wrapper around the WebVTT JavaScript parser. It was written to enable faster development of a WebVTT test suite. Th
e npm module includes the WebVTT parser, and allows one to pass file(s) in order to be validated.

## Installation

        npm install node-webvtt

installs the `webvtt.js` shell command.

## Examples

        webvtt.js file.vtt

        webvtt.js file1.vtt file2.vtt

        webvtt.js -s file.vtt

## Synopsis

        webvtt.js [options] <file...>

## Options

        -h, --help     output usage information

        -V, --version  output the version number

        -s, --silent   don't print errors messages

## Thanks

This project respectfully uses code from and thanks the authors of:

* [webvtt.js](https://bitbucket.org/annevk/webvtt)
* [commander](https://github.com/visionmedia/commander.js)
