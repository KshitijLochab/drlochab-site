// Pull the page data (conditions, procedures, guides, illustrations) out of the site source for EN and HI.
const fs=require('fs');
const [,,lang]=process.argv;
const src=fs.readFileSync(lang==='hi'?'site/hi/index.html':'site/index.html','utf8');
const script=src.match(/<script>([\s\S]*?)<\/script>/)[1];
const il=script.slice(script.indexOf('const IL='), script.indexOf('const ORGANS='));
const data=script.slice(script.indexOf('const ORGANS='), script.indexOf('const esc='));
const g0=script.indexOf('const GUIDES=['); const g1=script.indexOf('\n];',g0)+3;
const guides=script.slice(g0,g1);
const out=new Function(il+data+guides+'; return {IL,ORGANS,TIERS,SYMPTOMS,CONDITIONS,PROCS,MYTHS,GUIDES};')();
fs.writeFileSync(`data-${lang}.json`,JSON.stringify(out));
console.log(lang, Object.keys(out.IL).length, out.CONDITIONS.length, out.PROCS.length, out.GUIDES.length);
