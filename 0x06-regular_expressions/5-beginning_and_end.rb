#!/usr/bin/env ruby
regex = /^h.n$/
read = ARGV[0].scan(regex)
for a in read do
    print(a)
end
print("\n")
