# Deploying Your GRC Portfolio with GitHub Pages

This guide will walk you through the process of publishing your GRC portfolio as a professional website using GitHub Pages. GitHub Pages is a free hosting service that takes your portfolio files directly from your GitHub repository and publishes them online, making it easy to share your work with potential employers.

## What is GitHub Pages?

GitHub Pages is a static site hosting service provided by GitHub that publishes websites directly from a GitHub repository. It's perfect for hosting your GRC portfolio because:

- It's completely free
- It integrates seamlessly with your GitHub repository
- It provides a professional URL for your portfolio
- It supports custom domains if you want to use your own domain name
- It automatically updates when you update your repository

## Prerequisites

Before you begin, ensure you have:

1. A GitHub account
2. A forked or cloned copy of the GRC Portfolio Hub repository
3. Customized one of the portfolio templates with your information

## Step 1: Prepare Your Repository

The main approaches for setting up your portfolio repository:

### Option A: Fork the GRC Portfolio Hub

1. Visit the [GRC Portfolio Hub repository](https://github.com/yourusername/GRC_Portfolio)
2. Click the "Fork" button in the top-right corner to create your own copy
3. Rename your forked repository to `yourusername.github.io` for the cleanest URL

### Option B: Create a New Repository

If you prefer to start fresh:

1. Create a new repository named `yourusername.github.io`
2. Clone it to your local machine
3. Copy your customized portfolio files into this repository

## Step 2: Structure Your Portfolio Repository

For the best results with GitHub Pages, structure your repository as follows:

1. Move your customized portfolio (e.g., from the beginner or advanced template) to a file named `index.md` or `README.md` at the root of your repository
2. If using the advanced template with images, ensure all image paths are correct
3. Add any supporting files (PDFs, additional markdown files, images) to appropriate folders

Example structure:
```
yourusername.github.io/
├── index.md (or README.md) - Your main portfolio content
├── assets/
│   ├── images/
│   │   └── project-screenshots, diagrams, etc.
│   └── docs/
│       └── additional documentation, PDFs, etc.
└── projects/
    └── detailed-project-pages.md
```

## Step 3: Enable GitHub Pages

To publish your portfolio:

1. Go to your repository on GitHub
2. Click on "Settings" in the top navigation bar
3. Scroll down to the "GitHub Pages" section (or click "Pages" in the left sidebar for newer GitHub interfaces)
4. Under "Source", select the branch you want to publish (usually `main` or `master`)
5. For "Folder", select "/ (root)"
6. Click "Save"

GitHub will display a message with the URL where your site is published (usually `https://yourusername.github.io`).

## Step 4: Choose a Theme (Optional)

GitHub Pages supports Jekyll themes that can enhance the appearance of your portfolio:

1. In the same GitHub Pages settings section
2. Click "Choose a theme" or "Theme Chooser"
3. Browse the available themes and select one that complements your portfolio content
4. Click "Select theme"

## Step 5: Custom Domain (Optional)

If you own a domain name, you can use it for your portfolio:

1. In your GitHub Pages settings
2. Under "Custom domain", enter your domain name (e.g., `www.yourname.com`)
3. Click "Save"
4. Configure your domain's DNS settings:
   - For a subdomain (www): Add a CNAME record pointing to `yourusername.github.io`
   - For an apex domain: Add A records pointing to GitHub's IP addresses
5. Enable HTTPS by checking the "Enforce HTTPS" option (after DNS is configured)

## Step 6: Verify Your Portfolio

After GitHub Pages has built your site (which may take a few minutes):

1. Visit your published URL (`https://yourusername.github.io`)
2. Check all links, images, and formatting
3. Test the site on both desktop and mobile devices
4. Ensure all your projects and skills are displayed correctly

## Step 7: Add the URL to Your Resume and LinkedIn

Now that your portfolio is live, promote it:

1. Add the URL to your resume
2. Include it in your LinkedIn profile:
   - Go to your LinkedIn profile
   - Click the "Add profile section" button
   - Select "Websites" under the "Contact info" section
   - Enter your portfolio URL and a title like "GRC Portfolio"
3. Consider creating a LinkedIn post announcing your new portfolio

## Troubleshooting

If your site doesn't appear or has formatting issues:

1. **Build Errors**: Check the "Actions" tab of your repository to see if there are any build errors
2. **Markdown Formatting**: Ensure your markdown syntax is correct
3. **Image Paths**: Verify that all image paths are correct (use relative paths)
4. **Theme Compatibility**: Some themes may affect your custom formatting; try a different theme or use custom CSS
5. **Wait Time**: Sometimes GitHub Pages takes a few minutes to update after changes

## Advanced Customization

For more advanced customization:

1. **Custom CSS**: Create a file at `/assets/css/style.scss` with:
   ```scss
   @import "{{ site.theme }}";
   
   /* Your custom CSS here */
   body {
     font-family: 'Arial', sans-serif;
   }
   ```

2. **Custom Layout**: Create a `_layouts/default.html` file to customize your theme's layout

3. **Jekyll Configuration**: Add a `_config.yml` file to set site-wide variables:
   ```yml
   title: Your Name - GRC Professional
   description: AWS Security & Compliance Portfolio
   theme: jekyll-theme-minimal
   ```

## Keeping Your Portfolio Updated

Remember to keep your portfolio current:

1. Update it whenever you complete new labs or projects
2. Add new skills or certifications as you acquire them
3. Refresh quantifiable results and achievements regularly
4. Git commits will automatically trigger rebuilds of your GitHub Pages site

## Need Help?

If you encounter any issues with GitHub Pages deployment:

1. Consult the [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Check the [Common GitHub Pages issues](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)
3. Open an issue in the GRC Portfolio Hub repository for community assistance

---

Remember that your portfolio is a living document that showcases your skills and experience. Keep it updated and ensure it reflects your current capabilities and career goals. 