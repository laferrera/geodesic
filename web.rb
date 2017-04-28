require 'sinatra'
require 'Open3'
include Open3

get '/' do
  erb :index
end

post '/hull' do
  points = params["data"].split(',')
  num_points = points.shift
  point_data = "3\n" + num_points.to_s + "\n"
  i = 0
  while i < points.size do
    point_data += points[i].to_s + " " + points[i + 1].to_s + " " + points[i + 2].to_s + "\n"
    i += 3
  end
  puts "==============="
  puts point_data
  puts "==============="  
  #o, e, s = Open3.capture3("echo a; sort >&2", :stdin_data=>"foo\nbar\nbaz\n")
  o, e, s = Open3.capture3("bin/qhull i", :stdin_data => point_data)
  return o
end

set :public_folder, File.dirname(__FILE__) + '/static'