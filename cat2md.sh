#!/bin/bash

echo -e "## $1" >> report.md
echo -e "\`\`\`python" >> report.md
cat $1 >> report.md
echo -e "\`\`\`\n" >> report.md
