

rawurlencode() {
  local string="${1}"
  local strlen=${#string}
  local encoded=""
  local pos c o

  for (( pos=0 ; pos<strlen ; pos++ )); do
     c=${string:$pos:1}
     case "$c" in
        [-_.~a-zA-Z0-9] ) o="${c}" ;;
        * )               printf -v o '%%%02x' "'$c"
     esac
     encoded+="${o}"
  done
  echo "${encoded}"    # You can either set a return variable (FASTER) 
  REPLY="${encoded}"   #+or echo the result (EASIER)... or both... :p
}

session() {
    typeset -i length; length=$1
    typeset -i rounds; rounds=$2
    [ $rounds -lt 1 ] && rounds=1
    [ $length -lt 1 ] && {
        echo "Usage: $0 <length> [<rounds>]" 2>/dev/null; exit 1;
    }
    for ((i=0; i < $rounds; i++)); do
        for ((j=0; j < $length; j++)); do
            set=$(($RANDOM % 20))
            if   [ $set -le 6 ];  then o=65; l=26; # 35% uppercase
            elif [ $set -le 13 ]; then o=97; l=26; # 35% lowercase
            elif [ $set -le 17 ]; then o=48; l=10; # 20% numeric
    #        elif [ $set -le 18 ]; then o=58; l=7;  # 10% symbolic
    #        elif [ $set -le 19 ]; then o=33; l=15; 
        else ((j--)); continue
        fi
            ord=$(($o + $RANDOM % $l))
            printf \\$(($ord / 64 * 100 + $ord % 64 / 8 * 10 + $ord % 8))
        done
        echo
    done
}

sess=$(session 24)

while test -e . 
do
    echo -n 'q: '
    read q
    curl http://localhost:8989/api/v1.0/ask?question=$( rawurlencode "$q" )\&sessionid=$sess
done
