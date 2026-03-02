#!/bin/bash
# ============================================================
# DSA Patterns — GitHub Setup Script
# Run this ONCE from inside the dsa-patterns/ folder
# ============================================================
# Usage:
#   chmod +x setup.sh
#   ./setup.sh YOUR_GITHUB_USERNAME dsa-patterns
# ============================================================

USERNAME=$1
REPO_NAME=${2:-dsa-patterns}

if [ -z "$USERNAME" ]; then
  echo "❌ Error: Please provide your GitHub username"
  echo "   Usage: ./setup.sh YOUR_USERNAME"
  exit 1
fi

echo "🚀 Setting up DSA Patterns repo for GitHub..."

# Initialize git
git init
git add .
git commit -m "🎉 initial commit: DSA patterns repo structure"

# Set remote and push
echo ""
echo "⚠️  Make sure you've already created a repo called '$REPO_NAME' on GitHub!"
echo "   Go to: https://github.com/new"
echo ""
read -p "Press ENTER when your GitHub repo is ready..."

git branch -M main
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"
git push -u origin main

echo ""
echo "✅ Done! Your repo is live at:"
echo "   https://github.com/$USERNAME/$REPO_NAME"
echo ""
echo "📌 From now on, after Claude generates files for you, just run:"
echo "   git add ."
echo "   git commit -m 'your message'"
echo "   git push"
