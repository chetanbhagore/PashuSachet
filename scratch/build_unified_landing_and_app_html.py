import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load the 190 required IDs
with open("scratch/all_ids.json", "r", encoding="utf-8") as f:
    required_ids = json.load(f)

print(f"Loaded {len(required_ids)} required IDs to verify.")

# Read the App Shell HTML body from build_village_notebook_html.py
with open("scratch/build_village_notebook_html.py", "r", encoding="utf-8") as f:
    orig_code = f.read()

# Extract from '<header class="site-topbar">' down to '</body>'
start_idx = orig_code.find('<header class="site-topbar">')
end_idx = orig_code.find('<!-- SCRIPTS -->')
if start_idx == -1 or end_idx == -1:
    print("Error: Could not find markers in build_village_notebook_html.py")
    sys.exit(1)

app_shell_body = orig_code[start_idx:end_idx]

# Build the complete Landing + Role Select + App Shell HTML
landing_html = """<!DOCTYPE html>
<html lang="mr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>PashuSachet (पशूसचेत) — The Village Animal-Care Notebook | गावपातळीवरील पशू आरोग्य साथी</title>
  <meta name="description" content="PashuSachet — महाराष्ट्र शासन पशुसंवर्धन विभाग संलग्न गावपातळीवरील आधुनिक पशू आरोग्य नोंदवही. ९०-सेकंद लक्षण तपासणी, १९६२ फिरते पथक व पशू आधार.">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/landing.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <!-- ======================================================================
       1. PUBLIC LANDING PAGE (Public Marketing & Government Alignment)
       ====================================================================== -->
  <div id="publicLandingPage" class="landing-page-wrapper">
    
    <!-- LANDING NAVIGATION BAR -->
    <header class="landing-topbar">
      <div class="landing-brand" onclick="showLandingPage()">
        <div class="landing-brand-logo">
          <span data-icon="shield" data-size="22"></span>
        </div>
        <div>
          <div class="landing-brand-name">PashuSachet पशूसचेत</div>
          <div class="landing-brand-sub">महाराष्ट्र शासन पशुसंवर्धन विभाग संलग्न</div>
        </div>
      </div>

      <div class="landing-nav-actions">
        <a href="tel:1962" class="landing-1962-pill">
          <span data-icon="phone-call" data-size="14"></span>
          <span>1962 टोल-फ्री</span>
        </a>
        <button type="button" class="lang-switch-btn" onclick="toggleLanguage()">
          <span id="landingLangText">EN</span>
        </button>
        <button type="button" class="landing-btn-secondary" onclick="showRoleSelectScreen()">
          <span data-icon="user" data-size="14"></span>
          <span>भूमिका निवडा (Select Role)</span>
        </button>
        <button type="button" class="landing-btn-primary" onclick="startFarmerTriage()">
          <span data-icon="stethoscope" data-size="15"></span>
          <span>तपासणी सुरू करा</span>
        </button>
      </div>
    </header>

    <!-- HERO SECTION -->
    <section class="landing-hero">
      <div class="landing-hero-inner">
        <div>
          <div class="hero-pill-badge">
            <span data-icon="shield" data-size="14"></span>
            <span>पशु आरोग्य साथी • राष्ट्रीय गोकुळ मिशन व भारत पशुधन अनुरूप</span>
          </div>

          <h1 class="hero-main-title">
            गावपातळीवरील आधुनिक पशू आरोग्य नोंदवही
          </h1>

          <p class="hero-lead-text">
            जनावरांचे आजार वेळेवर ओळखा, ९० सेकंदात प्राथमिक लक्षण तपासणी करा, १९६२ फिरते पशुवैद्यकीय पथक बोलवा आणि दूध सुरक्षा लॉकसह प्रतिजैविक विथड्रॉवल नियम पाळा.
          </p>

          <div class="hero-cta-group">
            <button type="button" class="hero-cta-btn-lg" onclick="startFarmerTriage()">
              <span data-icon="stethoscope" data-size="18"></span>
              <span>मोफत तपासणी सुरू करा →</span>
            </button>
            <button type="button" class="hero-demo-btn-lg" onclick="showRoleSelectScreen()">
              <span data-icon="user" data-size="16"></span>
              <span>डेमो खात्यात प्रवेश करा</span>
            </button>
          </div>

          <div class="hero-trust-bullets">
            <div class="hero-trust-bullet">
              <span data-icon="check-circle-2" data-size="14" style="color: var(--status-success);"></span>
              <span>१००% मोफत व सुरक्षित</span>
            </div>
            <div class="hero-trust-bullet">
              <span data-icon="tag" data-size="14" style="color: var(--status-success);"></span>
              <span>१२-अंकी पशू आधार टॅग मान्यता</span>
            </div>
            <div class="hero-trust-bullet">
              <span data-icon="wifi-off" data-size="14" style="color: var(--status-success);"></span>
              <span>ऑफलाइन सक्षम (इंटरनेट नसतानाही)</span>
            </div>
          </div>
        </div>

        <!-- HERO PREVIEW CARD -->
        <div class="hero-visual-card">
          <div class="hero-visual-top">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="status-tag success">नोंदवही पूर्वावलोकन</span>
              <span style="font-size: 12px; color: var(--ink-secondary);">मौजे साक्री, जि. धुळे</span>
            </div>
            <span style="font-size: 11px; font-weight: 600; color: var(--status-success);">लाइव्ह सिंक सक्षम</span>
          </div>

          <div class="hero-visual-body">
            <!-- Animal Card 1 -->
            <div class="hero-animal-preview">
              <div class="hero-animal-avatar">
                <span data-icon="shield" data-size="24"></span>
              </div>
              <div style="flex: 1;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 15px;">गौरी (Gir Cow)</strong>
                  <span class="ear-tag-badge">240019283741</span>
                </div>
                <div style="font-size: 12px; color: var(--ink-secondary); margin-top: 2px;">
                  वय: ४ वर्षे • दुग्ध: १२ लि./दिवस • निरोगी
                </div>
              </div>
            </div>

            <!-- Animal Card 2 with Milk Lock -->
            <div class="hero-animal-preview" style="border-left: 3px solid var(--urgency-critical);">
              <div class="hero-animal-avatar" style="color: var(--urgency-critical);">
                <span data-icon="milk" data-size="24"></span>
              </div>
              <div style="flex: 1;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="font-size: 15px;">लक्ष्मी (Murrah Buffalo)</strong>
                  <span class="status-tag warning">दूध लॉक: ४८ तास</span>
                </div>
                <div style="font-size: 12px; color: var(--ink-secondary); margin-top: 2px;">
                  ऑक्सिटेट्रासायक्लिन विथड्रॉवल चालू • डेअरी सुरक्षा अलर्ट
                </div>
              </div>
            </div>

            <div style="margin-top: 8px; display: flex; justify-content: space-between; align-items: center; padding: 12px; background: var(--bg-paper-light); border-radius: var(--radius-sm);">
              <span style="font-size: 13px; font-weight: 600; color: var(--ink-primary);">जलद ९०-सेकंद लक्षण तपासणी:</span>
              <button type="button" class="btn-passport-sm primary" style="flex: 0 0 auto; padding: 6px 14px;" onclick="startFarmerTriage()">
                तपासा →
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- GOVERNMENT TRUST & ALIGNMENT BAR -->
    <div class="landing-trust-bar">
      <div class="trust-bar-inner">
        <div class="trust-item">
          <div class="trust-item-icon"><span data-icon="shield" data-size="20"></span></div>
          <div>
            <div class="trust-item-title">महाराष्ट्र शासन</div>
            <div class="trust-item-sub">पशुसंवर्धन विभाग संलग्न</div>
          </div>
        </div>

        <div class="trust-item">
          <div class="trust-item-icon"><span data-icon="tag" data-size="20"></span></div>
          <div>
            <div class="trust-item-title">भारत पशुधन (INAPH)</div>
            <div class="trust-item-sub">१२-अंकी डिजिटल टॅग सुसंगत</div>
          </div>
        </div>

        <div class="trust-item">
          <div class="trust-item-icon"><span data-icon="activity" data-size="20"></span></div>
          <div>
            <div class="trust-item-title">ICAR-NIVEDI</div>
            <div class="trust-item-sub">NADRES V2 रोग प्रादुर्भाव पूर्वसूचना</div>
          </div>
        </div>

        <div class="trust-item">
          <div class="trust-item-icon"><span data-icon="phone-call" data-size="20"></span></div>
          <div>
            <div class="trust-item-title">१९६२ रुग्णवाहिका (MVU)</div>
            <div class="trust-item-sub">तातडीचे फिरते पशुवैद्यकीय पथक</div>
          </div>
        </div>
      </div>
    </div>

    <!-- PROBLEM -> SOLUTION CONTRAST SECTION -->
    <section class="landing-section">
      <div class="section-header-centered">
        <span class="section-tag-pill">समस्या व समाधान • Problem & Solution</span>
        <h2 class="section-main-title">पारंपरिक अडचणींवर आधुनिक उपाय</h2>
        <p class="section-lead-sub">
          वेळेवर उपचार न मिळणे आणि दूध दूषित होण्यासारख्या गंभीर समस्यांवर पशूसचेतने दिलेले ठोस उपाय:
        </p>
      </div>

      <div class="problem-solution-grid">
        <!-- Card 1 -->
        <div class="contrast-card">
          <div class="contrast-problem-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--urgency-critical); text-transform: uppercase;">समस्या: आजारांची उशिरा ओळख</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              लक्षणे वेळेवर न समजल्याने लाळ्या खुरकूत किंवा लंपीसारखे संसर्गजन्य आजार संपूर्ण गावात पसरतात.
            </div>
          </div>
          <div class="contrast-solution-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--status-success); text-transform: uppercase;">पशूसचेत समाधान: ९०-सेकंद ट्रायज</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              सोपे लक्षण निवडून संभाव्य आजाराचा तात्काळ अंदाज, सुरक्षित प्रथमोपचार व पशु सखीकडून <३० सेकंद पडताळणी.
            </div>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="contrast-card">
          <div class="contrast-problem-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--urgency-critical); text-transform: uppercase;">समस्या: दुधातील प्रतिजैविक अवशेष (AMR)</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              अँटिबायोटिक उपचारादरम्यानचे दूध डेअरीमध्ये गेल्यास मानवी आरोग्यास धोका निर्माण होतो व डेअरीकडून दूध नाकारले जाते.
            </div>
          </div>
          <div class="contrast-solution-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--status-success); text-transform: uppercase;">पशूसचेत समाधान: दूध विथड्रॉवल लॉक</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              औषध दिल्यानंतर आपोआप विथड्रॉवल काउंटडाउन सुरू होते; दूध सुरक्षित होईपर्यंत डेअरी बंदी सूचना दिसते.
            </div>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="contrast-card">
          <div class="contrast-problem-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--urgency-critical); text-transform: uppercase;">समस्या: दुर्गम भागातील डॉक्टरांची कमतरता</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              रात्रीच्या वेळी किंवा आपत्कालीन परिस्थितीत तालुक्याच्या गावी जाणे शेतकर्‍यांना शक्य होत नाही.
            </div>
          </div>
          <div class="contrast-solution-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--status-success); text-transform: uppercase;">पशूसचेत समाधान: १९६२ फिरते पथक (MVU)</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              आपत्कालीन लक्षणे दिसताच एका क्लिकवर १९६२ रुग्णवाहिकेला संदेश जातो व स्थानिक पशु सखी गोठ्यावर पोहोचते.
            </div>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="contrast-card">
          <div class="contrast-problem-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--urgency-critical); text-transform: uppercase;">समस्या: कागदी नोंदी हरवणे व लसीकरण चुकणे</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              कागदी पुस्तके खराब झाल्याने कोणत्या जनावराला कोणती लस कधी दिली याची माहिती राहत नाही.
            </div>
          </div>
          <div class="contrast-solution-pane">
            <div style="font-size: 11px; font-weight: 700; color: var(--status-success); text-transform: uppercase;">पशूसचेत समाधान: डिजिटल पशू आधार</div>
            <div style="font-size: 13px; color: var(--ink-primary); margin-top: 4px;">
              प्रत्येक जनावराचे संपूर्ण लसीकरण, वैद्यकीय इतिहास व मालकी हस्तांतरण मोबाईलमध्ये सुरक्षित राहते.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS (4 STEPS) -->
    <section class="landing-section" style="background: var(--bg-paper-light); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
      <div class="section-header-centered">
        <span class="section-tag-pill">कार्यपद्धती • How It Works</span>
        <h2 class="section-main-title">पशूसचेत कसे कार्य करते? (४ सोप्या पायऱ्या)</h2>
        <p class="section-lead-sub">
          कोणत्याही क्लिष्टतेशिवाय, गावपातळीवर अत्यंत सहजपणे वापरता येणारी ४-टप्प्यांची रचना:
        </p>
      </div>

      <div class="steps-horizontal-grid">
        <!-- Step 1 -->
        <div class="step-flow-card">
          <div class="step-num-circle">१</div>
          <strong style="font-size: 16px;">जनावर निवडा व लक्षणे सांगा</strong>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            गोठ्यातील आजारी जनावराचा टॅग निवडा आणि दिसणाऱ्या लक्षणांवर (ताप, तोंडात फोड, गाठी) एका स्पर्शात नोंद करा.
          </p>
        </div>

        <!-- Step 2 -->
        <div class="step-flow-card">
          <div class="step-num-circle">२</div>
          <strong style="font-size: 16px;">तात्काळ मार्गदर्शन व प्रथमोपचार</strong>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            प्रणाली तात्काळ आजाराची संभाव्य तीव्रता (गंभीर, तातडीची, मध्यम) ठरवते आणि सुरक्षित घरगुती प्रथमोपचार सुचवते.
          </p>
        </div>

        <!-- Step 3 -->
        <div class="step-flow-card">
          <div class="step-num-circle">३</div>
          <strong style="font-size: 16px;">पशु सखी प्रत्यक्ष पडताळणी</strong>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            गावातील प्रशिक्षित पशु सखीला संदेश मिळताच त्या प्रत्यक्ष गोठ्यात येऊन लक्षणांची ३० सेकंदात खात्री करतात.
          </p>
        </div>

        <!-- Step 4 -->
        <div class="step-flow-card">
          <div class="step-num-circle">४</div>
          <strong style="font-size: 16px;">शासकीय उपचार व १९६२ पथक</strong>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            तालुका पशुवैद्यकीय अधिकारी तपासणी करतात किंवा तातडीच्या वेळी १९६२ फिरते पथक गावात पाठवले जाते.
          </p>
        </div>
      </div>
    </section>

    <!-- GOVERNMENT SCHEMES & INTEGRATIONS -->
    <section class="landing-section">
      <div class="section-header-centered">
        <span class="section-tag-pill">शासकीय योजना जोडणी • Schemes & Ecosystem</span>
        <h2 class="section-main-title">अधिकृत राष्ट्रीय व राज्य योजनांशी सुसंगत</h2>
        <p class="section-lead-sub">
          पशूसचेत हे कोणत्याही खाजगी साच्यात नसून भारत सरकारच्या पशुसंवर्धन मानकांशी थेट जोडलेले आहे:
        </p>
      </div>

      <div class="problem-solution-grid">
        <div class="notebook-card" style="margin-bottom: 0;">
          <div style="color: var(--accent-turmeric); margin-bottom: 10px;"><span data-icon="tag" data-size="28"></span></div>
          <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 6px;">भारत पशुधन (INAPH)</h3>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            १२-अंकी कानातील बारकोड टॅग पडताळणी. जनावराचे वय, जात, लसीकरण व मालकी थेट राष्ट्रीय डेटाबेसशी जोडली जाते.
          </p>
        </div>

        <div class="notebook-card" style="margin-bottom: 0;">
          <div style="color: var(--status-success); margin-bottom: 10px;"><span data-icon="activity" data-size="28"></span></div>
          <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 6px;">NADRES V2 (ICAR-NIVEDI)</h3>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            राष्ट्रीय साथरोग प्रादुर्भाव पूर्वसूचना प्रणाली. गावात संशयित केस आढळल्यास ५ किमी परिघात आपोआप रिंग व्हॅक्सिनेशन अलर्ट.
          </p>
        </div>

        <div class="notebook-card" style="margin-bottom: 0;">
          <div style="color: var(--urgency-critical); margin-bottom: 10px;"><span data-icon="phone-call" data-size="28"></span></div>
          <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 6px;">१९६२ फिरते पशुवैद्यकीय रुग्णालय (MVU)</h3>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            अचानक मृत्यू किंवा गंभीर आजारात थेट जीपीएस ट्रॅक केलेले फिरते वाहन शेतकऱ्याच्या दारात पाठवण्याची व्यवस्था.
          </p>
        </div>

        <div class="notebook-card" style="margin-bottom: 0;">
          <div style="color: var(--status-info); margin-bottom: 10px;"><span data-icon="shield" data-size="28"></span></div>
          <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 6px;">राष्ट्रीय पशु रोग नियंत्रण (NADCP)</h3>
          <p style="font-size: 13px; color: var(--ink-secondary); line-height: 1.5;">
            लाळ्या खुरकूत (FMD) व ब्रुसेलोसिस निर्मूलन मोहिमेतील मोफत डोसचे वेळापत्रक थेट शेतकऱ्याच्या मोबाईलवर.
          </p>
        </div>
      </div>
    </section>

    <!-- WHO IS THIS FOR (STAKEHOLDER ROLE CARDS) -->
    <section class="landing-section" style="background: var(--bg-paper-light); border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
      <div class="section-header-centered">
        <span class="section-tag-pill">वापरकर्ते • Who Is This For</span>
        <h2 class="section-main-title">प्रत्येक घटकासाठी समर्पित कार्यक्षेत्र</h2>
        <p class="section-lead-sub">
          शेतकऱ्यापासून ते जिल्हाधिकाऱ्यांपर्यंत प्रत्येकासाठी वेगळी व सोपी व्यवस्था:
        </p>
      </div>

      <div class="role-showcase-grid">
        <!-- Farmer -->
        <div class="role-persona-card">
          <div class="role-avatar-badge" style="background: rgba(221, 167, 58, 0.15); color: #B58223;">
            <span data-icon="home" data-size="22"></span>
          </div>
          <div>
            <h3 style="font-size: 17px; font-weight: 700;">🧑‍🌾 शेतकरी (Shetkari)</h3>
            <p style="font-size: 13px; color: var(--ink-secondary); margin-top: 4px; line-height: 1.5;">
              घरबसल्या जनावरांचे आरोग्य, ९०-सेकंद तपासणी, दवाखान्यात अपॉइंटमेंट आणि दूध सुरक्षा लॉक.
            </p>
          </div>
          <button type="button" class="btn-passport-sm primary" onclick="enterAppAsRole('farmer')" style="margin-top: auto;">
            शेतकरी म्हणून पहा →
          </button>
        </div>

        <!-- Para-Vet -->
        <div class="role-persona-card">
          <div class="role-avatar-badge" style="background: rgba(51, 107, 81, 0.15); color: var(--status-success);">
            <span data-icon="clipboard-check" data-size="22"></span>
          </div>
          <div>
            <h3 style="font-size: 17px; font-weight: 700;">🩺 पशु सखी (Field Sentinel)</h3>
            <p style="font-size: 13px; color: var(--ink-secondary); margin-top: 4px; line-height: 1.5;">
              गावातील संशयित अहवाल ३० सेकंदात पडताळणे, नमुना संकलन आणि पशुवैद्यकांना त्वरित पूर्वसूचना.
            </p>
          </div>
          <button type="button" class="btn-passport-sm" onclick="enterAppAsRole('paravet')" style="margin-top: auto;">
            पशु सखी म्हणून पहा →
          </button>
        </div>

        <!-- Vet -->
        <div class="role-persona-card">
          <div class="role-avatar-badge" style="background: rgba(43, 108, 176, 0.12); color: var(--status-info);">
            <span data-icon="stethoscope" data-size="22"></span>
          </div>
          <div>
            <h3 style="font-size: 17px; font-weight: 700;">👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO)</h3>
            <p style="font-size: 13px; color: var(--ink-secondary); margin-top: 4px; line-height: 1.5;">
              दवाखाना ओपीडी तपासणी, क्लिनिकल नोंदी, डिजिटल प्रिस्क्रिप्शन व विथड्रॉवल कालावधी गणक.
            </p>
          </div>
          <button type="button" class="btn-passport-sm" onclick="enterAppAsRole('ldo')" style="margin-top: auto;">
            पशुवैद्यक म्हणून पहा →
          </button>
        </div>

        <!-- Collector -->
        <div class="role-persona-card">
          <div class="role-avatar-badge" style="background: rgba(184, 93, 67, 0.15); color: var(--urgency-critical);">
            <span data-icon="building-2" data-size="22"></span>
          </div>
          <div>
            <h3 style="font-size: 17px; font-weight: 700;">🏛️ जिल्हा नियंत्रण कक्ष (DVO)</h3>
            <p style="font-size: 13px; color: var(--ink-secondary); margin-top: 4px; line-height: 1.5;">
              गावनिहाय रोग प्रादुर्भाव नकाशा (GIS), ५ किमी प्रतिबंधात्मक झोन आणि सकाळची आपत्कालीन निर्णय रांग.
            </p>
          </div>
          <button type="button" class="btn-passport-sm" onclick="enterAppAsRole('collector')" style="margin-top: auto;">
            अधिकारी म्हणून पहा →
          </button>
        </div>
      </div>
    </section>

    <!-- PILOT IMPACT & METRICS BANNER -->
    <section class="landing-section">
      <div class="pilot-metrics-banner">
        <div>
          <div class="metric-big-num">३५+</div>
          <div class="metric-label-txt">साक्री व संगमनेर बीटमधील समाविष्ट गावे</div>
        </div>
        <div>
          <div class="metric-big-num">&lt; ३० से.</div>
          <div class="metric-label-txt">पशु सखी सरासरी प्रत्यक्ष पडताळणी वेळ</div>
        </div>
        <div>
          <div class="metric-big-num">०%</div>
          <div class="metric-label-txt">विथड्रॉवल काळातील दूध संकलन दूषितता</div>
        </div>
        <div>
          <div class="metric-big-num">१००%</div>
          <div class="metric-label-txt">१२-अंकी पशू आधार टॅग पडताळणी</div>
        </div>
      </div>
      <div style="text-align: center; margin-top: 10px; font-size: 12px; color: var(--ink-tertiary);">
        *प्रात्यक्षिक बीट डेटा (Demonstration & Pilot Simulation)
      </div>
    </section>

    <!-- FINAL CALL TO ACTION -->
    <section class="landing-section" style="padding-top: 20px;">
      <div class="final-cta-card">
        <h2 style="font-family: var(--font-display); font-size: 30px; font-weight: 800; color: var(--ink-primary); margin-bottom: 12px;">
          आपल्या जनावरांची आरोग्य नोंद आजच सुरू करा
        </h2>
        <p style="font-size: 16px; color: var(--ink-secondary); max-width: 600px; margin: 0 auto 28px auto; line-height: 1.5;">
          शेतकऱ्यांसाठी १००% मोफत, सुरक्षित आणि महाराष्ट्र शासनाच्या पशुसंवर्धन मार्गदर्शक तत्त्वांनुसार विकसित.
        </p>
        <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
          <button type="button" class="hero-cta-btn-lg" onclick="startFarmerTriage()">
            <span data-icon="stethoscope" data-size="18"></span>
            <span>पशूसचेत सुरू करा (Open App)</span>
          </button>
          <button type="button" class="hero-demo-btn-lg" onclick="showRoleSelectScreen()">
            <span>प्रणाली प्रवेश / भूमिका निवडा →</span>
          </button>
        </div>
      </div>
    </section>

    <!-- PUBLIC FOOTER -->
    <footer class="landing-footer">
      <div style="max-width: 1120px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
        <div style="text-align: left;">
          <strong>PashuSachet (पशूसचेत — पशु आरोग्य साथी)</strong>
          <div style="margin-top: 4px; font-size: 12px;">पशुसंवर्धन व दुग्धव्यवसाय विकास विभाग, महाराष्ट्र शासन संलग्न • Built for Rural Maharashtra</div>
        </div>
        <div style="display: flex; gap: 14px; align-items: center;">
          <a href="tel:1962" style="color: var(--urgency-critical); font-weight: 700; text-decoration: none;">१९६२ आपत्कालीन पथक</a>
          <button type="button" class="btn-passport-sm" onclick="showRoleSelectScreen()" style="padding: 6px 14px;">लॉगिन करा</button>
        </div>
      </div>
    </footer>

  </div>

  <!-- ======================================================================
       2. INLINE ROLE SELECTION SCREEN (Shown when user clicks Login / Select Role)
       ====================================================================== -->
  <div id="publicRoleSelectScreen" class="public-role-select-container" style="display: none; padding: 40px 20px; min-height: 100vh; background: var(--bg-paper);">
    <div style="max-width: 680px; margin: 0 auto; background: #FFFFFF; border-radius: var(--radius-xl); padding: 36px 32px; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-modal);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <button type="button" class="landing-btn-secondary" onclick="showLandingPage()" style="padding: 6px 14px; font-size: 12.5px;">
          ← मुख्य पान (Back to Landing)
        </button>
        <span class="status-tag success">डेमो खाती उपलब्ध</span>
      </div>

      <div style="text-align: center; margin-bottom: 24px;">
        <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 800; color: var(--ink-primary);">
          प्रणाली प्रवेश: आपली भूमिका निवडा
        </h2>
        <p style="font-size: 13.5px; color: var(--ink-secondary); margin-top: 4px;">
          थेट कार्यक्षेत्रात प्रवेश करण्यासाठी योग्य कार्डवर स्पर्श करा:
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="role-choice-card" onclick="enterAppAsRole('farmer')">
          <div class="brand-emblem" style="color: var(--accent-turmeric);"><span data-icon="home" data-size="18"></span></div>
          <div style="flex: 1;">
            <div class="role-choice-title">🧑‍🌾 शेतकरी (Shetkari / Farmer)</div>
            <div class="role-choice-desc">एकनाथराव • मौजे साक्री (३ जनावरे) • ९०-सेकंद तपासणी व पशू आधार</div>
          </div>
          <span style="font-size: 13px; font-weight: 700; color: var(--accent-turmeric);">प्रवेश करा →</span>
        </div>

        <div class="role-choice-card" onclick="enterAppAsRole('paravet')">
          <div class="brand-emblem" style="color: var(--status-success);"><span data-icon="clipboard-check" data-size="18"></span></div>
          <div style="flex: 1;">
            <div class="role-choice-title">🩺 पशु सखी / पॅरा-व्हेट (Sentinel)</div>
            <div class="role-choice-desc">सुनिता पाटील • बीट साक्री व ५ गावे • पडताळणी रांग व नमुने</div>
          </div>
          <span style="font-size: 13px; font-weight: 700; color: var(--status-success);">प्रवेश करा →</span>
        </div>

        <div class="role-choice-card" onclick="enterAppAsRole('ldo')">
          <div class="brand-emblem" style="color: var(--status-info);"><span data-icon="stethoscope" data-size="18"></span></div>
          <div style="flex: 1;">
            <div class="role-choice-title">👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO Doctor)</div>
            <div class="role-choice-desc">डॉ. रामेश्वर कुटे • तालुका दवाखाना साक्री • ओपीडी व विथड्रॉवल</div>
          </div>
          <span style="font-size: 13px; font-weight: 700; color: var(--status-info);">प्रवेश करा →</span>
        </div>

        <div class="role-choice-card" onclick="enterAppAsRole('collector')">
          <div class="brand-emblem" style="color: var(--urgency-critical);"><span data-icon="building-2" data-size="18"></span></div>
          <div style="flex: 1;">
            <div class="role-choice-title">🏛️ जिल्हाधिकारी / DVO (Surveillance)</div>
            <div class="role-choice-desc">धुळे जिल्हा नियंत्रण कक्ष • ५ किमी रिंग व निर्णय रांग</div>
          </div>
          <span style="font-size: 13px; font-weight: 700; color: var(--urgency-critical);">प्रवेश करा →</span>
        </div>

        <div class="role-choice-card" onclick="enterAppAsRole('rddl')">
          <div class="brand-emblem" style="color: var(--ink-secondary);"><span data-icon="flask" data-size="18"></span></div>
          <div style="flex: 1;">
            <div class="role-choice-title">🔬 विभागीय प्रयोगशाळा (RDDL Lab)</div>
            <div class="role-choice-desc">पुणे मध्यवर्ती प्रयोगशाळा • RT-PCR नमुना ट्रॅकिंग व NADRES V2</div>
          </div>
          <span style="font-size: 13px; font-weight: 700; color: var(--ink-secondary);">प्रवेश करा →</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       3. AUTHENTICATED APP SHELL (The Full-Screen Village Care Notebook)
       ====================================================================== -->
  <div id="authenticatedAppShell" class="authenticated-app-shell" style="display: none;">
"""

# Now append the App Shell body from build_village_notebook_html.py
# (which contains the site-topbar, subnav, all 5 workspaces, all modals, and legacy-test-store)
# Add an "Exit to Landing" button in site-topbar
custom_topbar_action = """
      <button class="lang-switch-btn" onclick="showLandingPage()" title="मुख्य पानावर जा (Exit to Landing)">
        <span data-icon="home" data-size="13"></span>
        <span style="margin-left: 4px;">मुख्य पान</span>
      </button>
"""

modified_app_shell = app_shell_body.replace(
    '<button class="lang-switch-btn" id="langSwitchBtn"',
    custom_topbar_action + '      <button class="lang-switch-btn" id="langSwitchBtn"'
)

landing_html += modified_app_shell

landing_html += """
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toast"></div>

  <!-- SCRIPTS -->
  <script src="js/icons.js"></script>
  <script src="js/db.js"></script>
  <script src="js/app.js"></script>
  <script>
    // Public Routing & SPA Controller
    function showLandingPage() {
      document.getElementById('publicLandingPage').style.display = 'block';
      document.getElementById('publicRoleSelectScreen').style.display = 'none';
      document.getElementById('authenticatedAppShell').style.display = 'none';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function showRoleSelectScreen() {
      document.getElementById('publicLandingPage').style.display = 'none';
      document.getElementById('publicRoleSelectScreen').style.display = 'block';
      document.getElementById('authenticatedAppShell').style.display = 'none';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function showAppShell(role = 'farmer') {
      document.getElementById('publicLandingPage').style.display = 'none';
      document.getElementById('publicRoleSelectScreen').style.display = 'none';
      document.getElementById('authenticatedAppShell').style.display = 'block';
      if (typeof activatePersona === 'function') {
        activatePersona(role);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function startFarmerTriage() {
      showAppShell('farmer');
      if (typeof switchNotebookTab === 'function') {
        switchNotebookTab('viewFarmerTriage');
      }
      if (typeof goToTriageStep === 'function') {
        goToTriageStep(1);
      }
    }

    function enterAppAsRole(role) {
      try { localStorage.setItem('pashu_persona', role); } catch (e) {}
      showAppShell(role);
    }

    // Auto-route on load
    document.addEventListener('DOMContentLoaded', () => {
      const urlParams = new URLSearchParams(window.location.search);
      const roleParam = urlParams.get('role');
      const hash = window.location.hash;

      if (roleParam || hash === '#app') {
        showAppShell(roleParam || 'farmer');
      } else if (hash === '#login' || hash === '#select-role') {
        showRoleSelectScreen();
      } else {
        showLandingPage();
      }
    });
  </script>
</body>
</html>
"""

# Verify all 190 IDs are present in landing_html
missing_ids = []
for req_id in required_ids:
    if f'id="{req_id}"' not in landing_html and f"id='{req_id}'" not in landing_html:
        missing_ids.append(req_id)

if missing_ids:
    print(f"❌ ERROR: Missing {len(missing_ids)} required IDs in generated HTML!")
    print("Missing IDs:", missing_ids[:10])
    sys.exit(1)

print("✓ All 190 required IDs verified in generated unified HTML!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(landing_html)

print("Successfully written index.html with Landing Page + Role Selector + Authenticated App Shell!")
