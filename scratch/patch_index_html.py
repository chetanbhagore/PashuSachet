with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<button type="submit" class="btn btn-primary btn-lg" data-i18n="btn_analyze">'
replacement = '''<!-- Field Observation Notes / AI Vision / Voice Transcript -->
            <div class="form-group" style="margin-top: 14px; margin-bottom: 16px;">
              <label for="farmerVoiceNotes" style="font-weight: 700; color: #334155; display: flex; align-items: center; gap: 6px;">
                <span>📝 प्रत्यक्ष निरीक्षण नोंदी / AI फोटो तपासणी निष्कर्ष (Observation / AI Findings)</span>
              </label>
              <textarea id="farmerVoiceNotes" class="form-control" rows="2" placeholder="उदा. जनावराला २ दिवसांपासून ताप आहे, चारा खाणे बंद केले आहे किंवा AI व्हिजन निष्कर्ष..." style="font-size: 0.88rem; line-height: 1.4; resize: vertical;"></textarea>
            </div>

            <div style="display: flex; gap: 12px; align-items: center;">
              <button type="submit" id="triageSubmitBtn" class="btn btn-primary btn-lg" data-i18n="btn_analyze">'''

# Also remove the duplicate <div style="display: flex; gap: 12px; align-items: center;"> right before target
old_block = '''            <div style="display: flex; gap: 12px; align-items: center;">
              <button type="submit" class="btn btn-primary btn-lg" data-i18n="btn_analyze">'''

if old_block in html:
    html = html.replace(old_block, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Successfully patched index.html with farmerVoiceNotes and triageSubmitBtn!")
elif target in html:
    html = html.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Successfully patched target in index.html!")
else:
    print("❌ Target not found!")

