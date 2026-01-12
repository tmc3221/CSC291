#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <array>
#include <algorithm>

using namespace std;

// tone = 2
// semitone = 1
const vector<int> STEPS = {2, 2, 1, 2, 2, 2, 1};
const array<string, 12> NOTE_NAMES = {
    "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int number_notes;
  string n;
  cin >> number_notes;

  set<string> songNotes;
  set<string> scales;

  for (int i = 0; i < number_notes; i++) {
    cin >> n;
    songNotes.insert(n);
  }

  for (int i = 0; i < 12; i++) {
    // Build the scale notes via cumulative steps (with wraparound)
    set<string> scaleSet;
    int cur = i;
    scaleSet.insert(NOTE_NAMES[cur]);
    for (int step : STEPS) {
      cur = (cur + step) % 12;
      scaleSet.insert(NOTE_NAMES[cur]);
    }

    // Check: songNotes ⊆ scaleSet
    if (includes(scaleSet.begin(), scaleSet.end(),
                 songNotes.begin(), songNotes.end())) {
      scales.insert(NOTE_NAMES[i]);
    }
  }

  if (!scales.empty()) {
    // Print without trailing space
    string sep;
    for (const auto& note : scales) {
      cout << sep << note;
      sep = " ";
    }
    cout << '\n';
  } else {
    cout << "none\n";
  }

  return 0;
}

