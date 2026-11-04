# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Phase 5 helper...")

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

phase5_helper = """
// Fast-forward / Time travel simulation for Milk Withdrawal transition (TC-5.5)
function simulateFastForwardWithdrawal(tag = "MH-24-9812") {
  const animals = getStoredAnimals();
  const animal = animals.find(a => a.tag === tag);
  if (animal && animal.prescription) {
    // Offset prescribedAt to 10 days ago so treatment + withdrawal buffer has elapsed
    animal.prescription.prescribedAt = Date.now() - (10 * 24 * 3600 * 1000);
    try {
      localStorage.setItem("pashu_animals", JSON.stringify(animals));
    } catch(e) {}
    renderAnimals();
    updateWithdrawalClocks();
    showToast(`Withdrawal period for ${tag} fast-forwarded to EXPIRED (Milk Safe for Dairy)!`);
  }
}
"""

if "simulateFastForwardWithdrawal" not in js:
    js += "\n" + phase5_helper
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Added simulateFastForwardWithdrawal to js/app.js!")
else:
    print("simulateFastForwardWithdrawal already present in js/app.js!")

