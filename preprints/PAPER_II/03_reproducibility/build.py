"""Generate the delivered TeX from Markdown, then compile those exact TeX files."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
layout = Path(__file__).resolve().parent
def executable(name, fallback):
    return os.environ.get(name.upper()) or shutil.which(name) or str(Path.home()/fallback)
pandoc = executable("pandoc", ".cache/nw-typesetting/pandoc/pandoc-3.12.1/pandoc.exe")
tectonic = executable("tectonic", ".cache/nw-typesetting/tectonic/tectonic.exe")
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def codebreak(m):
    value=m[1].replace("/",r"/\allowbreak{}").replace(r"\_", r"\_\allowbreak{}").replace(".",r".\allowbreak{}")
    value=re.sub(r"(?<=[a-z])(?=[A-Z])",r"\\allowbreak{}",value)
    return r"\texttt{"+value+"}"
def compose(md):
    lang=md.stem[-2:]
    title,author,edition,body=md.read_text(encoding="utf8").split("\n\n",3)
    assert "jtraverso@gmail.com" in author and "0009-0003-6068-4096" in author
    series,version=(line.strip().strip("*") for line in edition.splitlines())
    title=title.removeprefix("# ").strip()
    body=subprocess.run([pandoc,"-f","markdown+tex_math_dollars","-t","latex","--wrap=none","--syntax-highlighting=none"],
                        input=body,encoding="utf8",capture_output=True,check=True).stdout
    body=re.sub(r"\\def\\LTcaptype\{none\}[^\n]*\n","",body)
    body=re.sub(r"\\texttt\{([^{}]*)\}",codebreak,body)
    body=re.sub(r"(?<![A-Za-z0-9/])([a-f0-9]{40})(?![A-Za-z0-9/])",
                lambda match:r"\allowbreak{}".join(match[1][i:i+10] for i in range(0,40,10)),body)
    body=re.sub(r"\\textbf\{([A-Za-z][A-Za-z0-9\\_]+)\}",
                lambda match:r"\textbf{"+match[1].replace(r"\_",r"\_\allowbreak{}")+"}",body)
    body=body.replace("ε-dense",r"\(\varepsilon\)-dense")
    body=re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{(figures/[^}]+)\}',r'\\includegraphics[width=.89\\linewidth]{\1}',body)
    body=body.replace(r"\begin{figure}",r"\begin{figure}[htbp]")
    if md.name.startswith("profiles_"):
        body=re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", lambda m: r"\Needspace{18\baselineskip}"+m[0] if ("Blocks added" in m[0] or "Bloques añadidos" in m[0]) else m[0], body, flags=re.S)
    if md.name.startswith("spectrum_"):
        body=body.replace(r".89\linewidth]{figures/fano.png}",r".48\linewidth]{figures/fano.png}")
        body=body.replace(r"\begin{longtable}",r"\Needspace{23\baselineskip}\begin{longtable}",1)
    body=re.sub(r"(\\textbf\{(?:Theorem|Teorema) 1[^}]*\})",r"\\Needspace{9\\baselineskip}\1",body)
    body=re.sub(r"(\\subsection\{(?:Use of artificial intelligence and computational tools|Uso de inteligencia artificial y herramientas computacionales)\})",r"\\Needspace{8\\baselineskip}\1",body)
    def lean_block(match):
        greek={"∀":r"\forall","∃":r"\exists","∧":r"\land","∨":r"\lor","¬":r"\neg",
               "ℕ":r"\mathbb N","ℤ":r"\mathbb Z","→":r"\to","↔":r"\leftrightarrow",
               "≤":r"\le","≥":r"\ge","₀":"_0","₂":"_2","∈":r"\in","≠":r"\ne"}
        escape={"_":r"\_\allowbreak{}","%":r"\%","{":r"\{","}":r"\}","^":r"\textasciicircum{}",
                "&":r"\&","#":r"\#","\\":r"\textbackslash{}"}
        rows=[]
        for line in match[1].splitlines():
            indent=len(line)-len(line.lstrip())
            rows.append(r"\noindent\hspace*{"+str(.45*indent)+"em}"+''.join(
                r"\("+greek[c]+r"\)" if c in greek else escape.get(c,c) for c in line.lstrip())+r"\par")
        return r"\begingroup\small\ttfamily\raggedright "+"\n"+"\n".join(rows)+r"\endgroup"
    body=re.sub(r"\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}",lean_block,body,flags=re.S)
    body=re.sub(r"(\\subsection\{(?:Appendix\. The formal characterization|Apéndice\. La caracterización formal)\})",r"\\Needspace{15\\baselineskip}\1",body)
    pre=(layout/f"series_{lang}.tex").read_text(encoding="utf8")
    tex=md.with_suffix(".tex")
    title_tex=title.replace("#",r"\#")
    text=pre+r"""
\usepackage{graphicx}
\providecommand{\pandocbounded}[1]{#1}
\hypersetup{pdftitle={"""+title_tex+r"""},pdfauthor={Juan Pablo Traverso Gianini},pdflang={"""+lang+r"""},colorlinks=true,linkcolor=blue,urlcolor=blue}
\title{"""+title_tex+r"""}
\author{Juan Pablo Traverso Gianini\\\small """+("Investigador independiente" if lang=="es" else "Independent researcher")+r""", Santiago, Chile\\\small \href{mailto:jtraverso@gmail.com}{jtraverso@gmail.com}\\\small \href{https://orcid.org/0009-0003-6068-4096}{ORCID: 0009-0003-6068-4096}}
\date{}
\begin{document}
\raggedbottom
\maketitle
"""+r"\textbf{"+series+r"}\\\textbf{"+version+"}\n\n"+body+"\n\\end{document}\n"
    tex.write_text(text,encoding="utf8",newline="\n")
    env=os.environ.copy()
    localcache=Path("C:/nw/physical-typed-absorption/tools/editorial-typesetting-runtime/cache")
    if "TECTONIC_CACHE_DIR" not in env and localcache.is_dir():
        env["TECTONIC_CACHE_DIR"]=str(localcache)
    with tempfile.TemporaryDirectory() as tmp:
        dest=Path(tmp)
        if os.name=="nt":
            fonts=dest/"fonts.conf"
            fonts.write_text('<fontconfig><dir>C:/Windows/Fonts</dir><cachedir prefix="xdg">fontconfig</cachedir></fontconfig>',encoding="utf8")
            env["FONTCONFIG_FILE"]=str(fonts)
        command=[tectonic,"--keep-logs","--outdir",str(dest)]
        if "TECTONIC_CACHE_DIR" in env:
            command.append("--only-cached")
        outputs=[]
        for pass_number in (1,2):
            run=subprocess.run(command+[str(tex.resolve())],cwd=md.parent,env=env,capture_output=True,encoding="utf8",errors="replace")
            outputs.append(run.stdout+run.stderr)
            if run.returncode:
                raise RuntimeError((run.stdout+run.stderr)[-5200:])
        log=(dest/tex.with_suffix(".log").name).read_text(encoding="utf8",errors="replace")
        issues=[line for line in log.splitlines() if re.search(r"Overfull|Missing character:|undefined references|LaTeX Error|undefined on input line",line)]
        pdf=md.with_suffix(".pdf")
        assert "Writing" in run.stdout+run.stderr and pdf.name in run.stdout+run.stderr
        shutil.copyfile(dest/pdf.name,pdf)
        logs=root/"02_validation/compiler_logs"
        logs.mkdir(exist_ok=True)
        logfile=logs/(md.stem+".log")
        logfile.write_text(log,encoding="utf8",newline="\n")
        (logs/(md.stem+".txt")).write_text("\n\n".join(outputs),encoding="utf8",newline="\n")
        print(pdf.name,ascii(issues),flush=True)
        return {"version":"1.0","md":digest(md),"tex":digest(tex),"pdf":digest(pdf),"layout_issues":issues,"compile_passes":2,"engine":"Tectonic","log":str(logfile.relative_to(root)).replace("\\","/"),"log_sha256":digest(logfile),"output_pdf":pdf.name}
if __name__=="__main__":
    sources=[root/s for s in sys.argv[1:]] or sorted((root/"01_manuscript").glob("*.md"))+sorted((root/"05_formalization").glob("companion_*.md"))
    for md in sources:
        record=compose(md)
        (root/"02_validation"/(md.stem+"_build.json")).write_text(json.dumps(record,indent=2)+"\n",encoding="utf8",newline="\n")
