#!/usr/bin/env ruby
# Find the regular expression that matches a string beginning with 'h' and ending with 'n' and can have any single character in between
# has to be exactly 3 characters long
puts ARGV[0].scan(/h.n/).join
