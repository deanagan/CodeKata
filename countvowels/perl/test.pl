#!/usr/bin/perl

use strict;
use warnings;

sub countvowels {
    my @params = @_;
    
    # set to lower case
    my $str = lc $params[0];

    my @matches = ($str =~ /[aeiou]/g);

    # Retrieves the length of matches
    my $total = @matches;

    return $total;
}

sub main() {
    my @strs = qw(hellO abracadabra these world totally);
    
    foreach my $str (@strs) {    
        print("$str has ".countvowels($str)." vowels.\n");
    }
}


main();
