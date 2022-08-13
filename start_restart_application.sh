Process_Number=$(ps aux | grep -v grep | grep 'python3 main.py' | awk '{print $2}')
if [[ -n $Process_Number ]]; then
    kill -9 $Process_Number
    echo "Killed Process number $Process_Number"
    nohup python3 main.py &
else
    echo "No process found"
    nohup python3 main.py &
fi
