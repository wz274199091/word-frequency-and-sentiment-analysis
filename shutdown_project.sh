#!/bin/bash


pid=$(cat pid.pid)


son_pid=$(pgrep -P $pid)

pids=($(pgrep -P $son_pid))

for item in "${pids[@]}"; do
  echo "Killing pool process with PID: $item"
  kill -9 $item
done

echo "Killing son process with PID: $son_pid"
kill -9 $son_pid

echo "Killing main process with PID: $pid"
kill -9 $pid