all:	ICMCL.docx

clean:
	rm -i ICMCL.docx

ICMCL.docx:	ICMCL.md
	pandoc -S -o ICMCL.docx --filter pandoc-citeproc --reference-docx=reference.docx ICMCL.md
