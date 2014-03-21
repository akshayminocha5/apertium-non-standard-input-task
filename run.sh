cat $1 | ./language_identifier.py > temp_language
if [ $# -ge 2 ]
then
  echo $2 > temp_language
fi

cat $1 | ./emoticon_remove_regexp.py |  ./repetitions_hahe.py | ./superblank_addition.py | ./easy_tokenize2.py | ./emoticons_remove.py | ./abbreviations_replace.py | ./original_candidate_format.py  | ./extended_words_trim2.py | ./apostrophe_correction.py | ./trie_implementation.py | ./selecting_best_candidate.py | ./escape_sequence_addition.py  
