#!/usr/bin/env ruby
# find the regex that matches the cases "hbn, hbtn, hbttn..., hbttttn"
puts ARGV[0].scan(/hbt{0,4}n/).join