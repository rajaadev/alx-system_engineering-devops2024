#!/usr/bin/env ruby
# Output the provided test string
puts ARGV[0].scan(/\b\d{10}\b/).join
