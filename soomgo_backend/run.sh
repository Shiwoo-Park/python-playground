INPUT_FILE=$1
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
PROGRAM_PATH="${SCRIPT_PATH}/main.py"

function join_by { local IFS="$1"; shift; echo "$*"; }

if [ -z ${INPUT_FILE} ]; then
  input_arr=()
  while read line
  do
    echo "$line"
    input_arr+=("$line")
  done < "${1:-/dev/stdin}"
else
  echo "222INPUT_FILE=${INPUT_FILE}"

fi


