#!/usr/bin/env ruby
# regex that pulls the capitol letters out of a string
puts ARGV[0].scan(/[A-Z]/).join
