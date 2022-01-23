from typing import Optional, Sequence, List
from flask import session


def flash(message: str, category: str = "message") -> None:
    flashes = session.get("_flashes", [])
    flashes.append((category, message))
    session["_flashes"] = flashes


def peek_flashed_messages(category_filter: Optional[Sequence] = None) -> List:
    # if category_filter is not provided, initialize to blank list
    if not category_filter: category_filter = []
    # safely get flashes from flask session storage
    flashes = session.get("_flashes", [])
    # shortcut, no messages, return empty list
    if not flashes: return []
    matches = []
    for category, message in flashes:
        if not category_filter:
            # no category filter is given, append flash to "matches"
            matches.append((category, message))
        else:
            if category in category_filter:
                # category filter specified, this flash's category matches provided list, append flash to "matches"
                matches.append((category, message))
    return matches


def get_flashed_messages(category_filter=None):
    # if category_filter is not provided, initialize to blank list
    if not category_filter: category_filter = []
    session.pop("_flashes") if "_flashes" in session else []
    all_messages = set(session.get("_flashes", []))
    matches = set(peek_flashed_messages(category_filter=category_filter))
    non_matching_messages = all_messages - matches
    session['_flashes'] = list(non_matching_messages)
    return list(matches)
