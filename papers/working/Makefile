all:	main.docx proposal.docx

clean:
	rm -i main.docx proposal.docx

main.docx:	main.md
	pandoc -S -o main.docx --filter pandoc-citeproc --reference-docx=reference.docx main.md

proposal.docx:	proposal.md
	pandoc -S -o proposal.docx --filter pandoc-citeproc --reference-docx=reference.docx proposal.md
