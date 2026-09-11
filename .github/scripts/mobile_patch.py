from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

s = s.replace('.serif{font-family:Iowan Old Style,Baskerville,"Times New Roman",serif}', '.serif{font-family:Georgia,"Times New Roman",serif}')
s = s.replace('backdrop-filter:blur(14px);border-bottom:1px solid var(--line)', '-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)')
s = s.replace('.lang{border:1px solid var(--line);background:transparent;border-radius:999px;padding:7px 11px;cursor:pointer}', '.lang{border:1px solid var(--line);background:transparent;border-radius:999px;padding:7px 11px;cursor:pointer;min-width:44px;min-height:44px}.menuBtn{display:none;border:1px solid var(--line);background:transparent;border-radius:999px;width:44px;height:44px;align-items:center;justify-content:center;cursor:pointer;font-size:1.15rem;line-height:1}')
s = s.replace('.filter{border:1px solid var(--line);background:transparent;border-radius:999px;padding:8px 13px;cursor:pointer}', '.filter{border:1px solid var(--line);background:transparent;border-radius:999px;padding:8px 13px;cursor:pointer;min-height:44px}')
s = s.replace('.close{position:absolute;right:22px;top:14px;border:0;background:transparent;color:white;font-size:2rem;cursor:pointer}', '.close{position:absolute;right:14px;top:10px;border:0;background:transparent;color:white;font-size:2rem;cursor:pointer;width:48px;height:48px;display:flex;align-items:center;justify-content:center}')
s = s.replace('.contactlinks a{display:block;width:max-content;font-size:1.25rem;padding:7px 0;border-bottom:1px solid var(--ink)}', '.contactlinks a{display:flex;align-items:center;width:max-content;min-height:44px;font-size:1.25rem;padding:7px 0;border-bottom:1px solid var(--ink)}')
s = s.replace('.hero{min-height:calc(100vh - 68px);display:grid;', '.hero{min-height:calc(100vh - 68px);min-height:calc(100svh - 68px);display:grid;')
s = s.replace('.heroimg{height:min(72vh,760px);overflow:hidden;', '.heroimg{height:min(72vh,760px);height:min(72svh,760px);overflow:hidden;')

old_mobile = '@media(max-width:620px){.wrap{width:calc(100% - 28px)}nav{height:60px}.links a{display:none}.hero{padding:32px 14px 0}.hero h1{font-size:20vw}.heroimg{height:52vh}.meta{gap:10px}section{padding:68px 0}.head{grid-template-columns:1fr;margin-bottom:34px}.work,.work.wide{grid-column:span 12}.thumb{aspect-ratio:1.2/1}.contactbox h2{font-size:23vw}.cvitem{grid-template-columns:52px 1fr}}'
new_mobile = '@media(max-width:620px){.wrap{width:calc(100% - 28px)}nav{height:60px;position:relative}.menuBtn{display:inline-flex}.links{gap:8px}.links>a{display:none}.links.open{position:absolute;left:-14px;right:-14px;top:60px;background:rgba(242,239,233,.98);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-bottom:1px solid var(--line);padding:10px 14px 16px;display:flex;flex-direction:column;align-items:stretch;gap:0;box-shadow:0 12px 24px rgba(23,22,20,.08)}.links.open>a{display:flex;align-items:center;min-height:46px;border-bottom:1px solid var(--line);font-size:.9rem}.links.open .lang{align-self:flex-start;margin-top:10px}.hero{padding:32px 14px 0}.hero h1{font-size:20vw}.heroimg{height:52vh;height:52svh}.meta{gap:10px}section{padding:68px 0}.head{grid-template-columns:1fr;margin-bottom:34px}.work,.work.wide{grid-column:span 12}.thumb{aspect-ratio:1.2/1}.contactbox h2{font-size:23vw}.cvitem{grid-template-columns:52px 1fr}.modal{padding:20px 14px 56px}.modal img{max-width:96vw;max-height:80svh}.modalcap{left:16px;right:16px;bottom:16px}}'
if old_mobile not in s:
    raise SystemExit('Expected mobile CSS block was not found')
s = s.replace(old_mobile, new_mobile)

old_nav = '<header><nav class="wrap"><a class="brand" href="#top">Elena Orlova</a><div class="links"><a href="#practice" data-en="Practice" data-ru="Практика">Practice</a><a href="#works" data-en="Works" data-ru="Работы">Works</a><a href="#projects">Art + Science</a><a href="#media" data-en="Media" data-ru="СМИ">Media</a><a href="#cv">CV</a><a href="#contact" data-en="Contact" data-ru="Контакты">Contact</a><button class="lang" id="lang">RU</button></div></nav></header>'
new_nav = '<header><nav class="wrap"><a class="brand" href="#top">Elena Orlova</a><div class="links" id="navLinks"><a href="#practice" data-en="Practice" data-ru="Практика">Practice</a><a href="#works" data-en="Works" data-ru="Работы">Works</a><a href="#projects">Art + Science</a><a href="#media" data-en="Media" data-ru="СМИ">Media</a><a href="#cv">CV</a><a href="#contact" data-en="Contact" data-ru="Контакты">Contact</a><button class="lang" id="lang">RU</button></div><button class="menuBtn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">☰</button></nav></header>'
if old_nav not in s:
    raise SystemExit('Expected navigation markup was not found')
s = s.replace(old_nav, new_nav)

mobile_js = """
const menuBtn=document.getElementById('menuBtn'),navLinks=document.getElementById('navLinks');
const closeMenu=()=>{if(!menuBtn||!navLinks)return;navLinks.classList.remove('open');menuBtn.setAttribute('aria-expanded','false');menuBtn.textContent='☰';menuBtn.setAttribute('aria-label','Open menu')};
if(menuBtn&&navLinks){menuBtn.addEventListener('click',()=>{const open=navLinks.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));menuBtn.textContent=open?'×':'☰';menuBtn.setAttribute('aria-label',open?'Close menu':'Open menu')});navLinks.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});window.addEventListener('resize',()=>{if(window.innerWidth>620)closeMenu()})}
"""
if "const menuBtn=document.getElementById(" not in s:
    pos = s.rfind('</script>')
    if pos == -1:
        raise SystemExit('Closing script tag not found')
    s = s[:pos] + mobile_js + s[pos:]

p.write_text(s, encoding='utf-8')
