#!/usr/bin/env node

var parser = require( "../lib/parser" ),
    fs = require( "fs" ),
    program = require( "commander" );

program
  .version( "0.0.1" )
  .usage( "[options] <file...>" )
  .option( "-s, --silent", "don't print errors messages" )
  .parse( process.argv );

var filenames = program.args,
    failed = false;

if( filenames.length < 1 ) {
  console.log( "Missing input file(s)." );
  console.log( "Usage: webvtt " + program.usage() );
  process.exit( 1 );
}

filenames.forEach( function( filename ) {
  try {
    var stats = fs.statSync( filename );
    if( !stats.isFile() ) {
      console.log( "webvtt: %s: Not a file.", filename );
      failed = true;
      return;
    }
  } catch( e ) {
    console.log( "webvtt: %s: No such file.", filename );
    failed = true;
    return;
  }

  var data = fs.readFileSync( filename, "utf-8" );
  if( !data ) {
    console.log( "webvtt: %s: Error - %s", filename, err.message );
    failed = true;
    return;
  }

  // Strip optional Unicode BOM character
  data = data.replace( /^\uFEFF/, '' );

  var r = ( new parser.WebVTTParser() ).parse( data ),
      errors = r.errors,
      error;

  for( var i = 0; i < errors.length; i++ ) {
    failed = true;
    error = errors[ i ];
    if( !program.silent ) {
      // sourcefile:lineno.column: message
      console.log( "%s:%s.%s: %s", filename, error.line, error.col|0, error.message );
    }
  }
});

process.exit( failed ? 1 : 0 );
