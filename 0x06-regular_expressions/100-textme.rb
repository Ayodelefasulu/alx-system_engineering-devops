#!/usr/bin/env ruby

def extract_message_info(log_entry)
  sender = log_entry.match(/\[from:([^\]]+)\]/)&.captures&.first
  receiver = log_entry.match(/\[to:([^\]]+)\]/)&.captures&.first
  flags = log_entry.match(/\[flags:([^\]]+)\]/)&.captures&.first

  puts "#{sender},#{receiver},#{flags}" if sender && receiver && flags
end

# Iterate over command line arguments
ARGV.each do |arg|
  # Extract information from the log entry
  extract_message_info(arg) if arg.include?("Receive SMS") || arg.include?("Sent SMS")
end
