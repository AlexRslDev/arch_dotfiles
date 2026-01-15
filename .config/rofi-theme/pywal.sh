#!/usr/bin/env bash

# Color files
RFILE="$HOME/.config/rofi-theme/rofi/colors.rasi"
WFILE="$HOME/.cache/wal/colors.sh"

# Get colors
pywal_get() {
  wal -i "$1" -q -t
}

# Change colors
change_color() {
  # rofi
  cat >$RFILE <<-EOF
	/* colors */

	* {
	  al:    #00000000;
	  bg:    ${BG}FF;
	  ac:    ${AC}FF;
	  se:    ${AC}26;
	  fg:    ${FG}FF;
	}
	EOF
}

# Main
if [[ -x "$(which wal)" ]]; then
  if [[ "$1" ]]; then
    pywal_get "$1"

    # Source the pywal color file
    if [[ -e "$WFILE" ]]; then
      . "$WFILE"
    else
      echo 'Color file does not exist, exiting...'
      exit 1
    fi

    BG=$(printf "%s\n" "$background")
    FG=$(printf "%s\n" "$foreground")
    AC=$(printf "%s\n" "$color1")

    change_color
  else
    echo -e "[!] Please enter the path to wallpaper. \n"
    echo "Usage : ./pywal.sh path/to/image"
  fi
else
  echo "[!] 'pywal' is not installed."
fi
