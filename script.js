/**
 * Logistics Management System Website Scripts
 * This file contains all the JavaScript functionality for the website
 * including navigation, security measures, and interactive elements.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize mobile menu functionality
    initializeMobileMenu();

    // Initialize code highlighting
    initializeCodeHighlighting();

    // Add security measures
    implementSecurityMeasures();

    // Initialize smooth scrolling
    initializeSmoothScrolling();

    // Setup citation references
    setupCitationReferences();
});

/**
 * Initializes the mobile menu toggle functionality
 */
function initializeMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function() {
            navLinks.classList.toggle('active');

            // Update aria-expanded attribute for accessibility
            const isExpanded = navLinks.classList.contains('active');
            mobileMenuBtn.setAttribute('aria-expanded', isExpanded);
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('nav') && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuBtn.setAttribute('aria-expanded', false);
            }
        });
    }
}

/**
 * Initializes syntax highlighting for code blocks using Prism.js
 */
function initializeCodeHighlighting() {
    // Prism.js is loaded from CDN in the HTML file
    // This function can be used to add any custom behaviors for code blocks

    // Add copy code button to code blocks
    const codeBlocks = document.querySelectorAll('.code-example pre');

    codeBlocks.forEach(block => {
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-code-btn';
        copyButton.textContent = 'Copy';

        const codeHeader = block.parentElement.querySelector('.code-header');
        if (codeHeader) {
            codeHeader.appendChild(copyButton);

            copyButton.addEventListener('click', () => {
                const code = block.textContent;
                copyToClipboard(code, copyButton);
            });
        }
    });
}

/**
 * Implements various security measures for the website
 */
function implementSecurityMeasures() {
    // 1. Content Security Policy (CSP) - Applied via meta tag in HTML

    // 2. Sanitize any user input
    document.querySelectorAll('input, textarea').forEach(input => {
        input.addEventListener('input', function() {
            this.value = sanitizeInput(this.value);
        });
    });

    // 3. Add CSRF token to forms
    document.querySelectorAll('form').forEach(form => {
        addCSRFToken(form);
    });

    // 4. Prevent XSS in URL parameters
    sanitizeUrlParameters();

    // 5. Protect against clickjacking by setting X-Frame-Options header
    // (This would normally be set on the server, but we can check client-side)
    checkFraming();

    // 6. Implement subresource integrity for external scripts
    validateSubresourceIntegrity();
}

/**
 * Sanitizes user input to prevent XSS attacks
 * @param {string} input - The user input to sanitize
 * @return {string} - Sanitized input
 */
function sanitizeInput(input) {
    // Basic XSS prevention
    return input
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');
}

/**
 * Adds CSRF token to forms to prevent cross-site request forgery
 * @param {HTMLFormElement} form - The form to add the token to
 */
function addCSRFToken(form) {
    // In a real application, the CSRF token would be generated server-side
    // This is a simplified example for demonstration purposes
    const csrfToken = generateCSRFToken();

    // Add or update the CSRF token input
    let tokenInput = form.querySelector('input[name="csrf_token"]');

    if (!tokenInput) {
        tokenInput = document.createElement('input');
        tokenInput.type = 'hidden';
        tokenInput.name = 'csrf_token';
        form.appendChild(tokenInput);
    }

    tokenInput.value = csrfToken;

    // Store the token in localStorage or sessionStorage
    sessionStorage.setItem('csrf_token', csrfToken);
}

/**
 * Generates a simple CSRF token
 * @return {string} - Generated token
 */
function generateCSRFToken() {
    // In a real application, this would be generated server-side
    return Math.random().toString(36).substring(2) + Date.now().toString(36);
}

/**
 * Sanitizes URL parameters to prevent XSS attacks
 */
function sanitizeUrlParameters() {
    const urlParams = new URLSearchParams(window.location.search);

    // Check each parameter for potential XSS
    for (const [key, value] of urlParams.entries()) {
        if (containsXSSAttempt(value)) {
            // Remove the parameter
            urlParams.delete(key);

            // Log the attempt (in a real application, this might send to a security monitoring service)
            console.warn(`Potential XSS attempt detected in URL parameter "${key}"`);
        }
    }

    // Update the URL if changes were made (without page reload)
    const newUrl = window.location.pathname + (urlParams.toString() ? `?${urlParams.toString()}` : '');
    window.history.replaceState({}, document.title, newUrl);
}

/**
 * Checks if a string contains potential XSS payloads
 * @param {string} value - The string to check
 * @return {boolean} - True if potential XSS is detected
 */
function containsXSSAttempt(value) {
    // Check for common XSS patterns
    const xssPatterns = [
        /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,
        /javascript:/gi,
        /on\w+=/gi,
        /data:/gi
    ];

    return xssPatterns.some(pattern => pattern.test(value));
}

/**
 * Checks if the page is being framed and blocks it if necessary
 */
function checkFraming() {
    // Prevent the page from being loaded in an iframe to prevent clickjacking
    if (window.self !== window.top) {
        // Page is being framed
        document.body.innerHTML = `
            <div class="security-alert">
                <h4>Security Alert</h4>
                <p>This page cannot be displayed in a frame to prevent clickjacking attacks.</p>
            </div>
        `;
    }
}

/**
 * Validates subresource integrity for external scripts and stylesheets
 */
function validateSubresourceIntegrity() {
    const externalResources = document.querySelectorAll('script[src], link[rel="stylesheet"]');

    externalResources.forEach(resource => {
        // Check if the resource has an integrity attribute
        if (!resource.hasAttribute('integrity') && !resource.src?.includes(window.location.hostname)) {
            console.warn(`External resource without SRI: ${resource.src || resource.href}`);

            // In a real application, you might want to dynamically add integrity attributes
            // or prevent loading of resources without integrity checks
        }
    });
}

/**
 * Copies text to clipboard with a visual feedback
 * @param {string} text - Text to copy
 * @param {HTMLElement} button - Button element for feedback
 */
function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text)
        .then(() => {
            // Show success feedback
            const originalText = button.textContent;
            button.textContent = 'Copied!';
            button.style.backgroundColor = '#10b981';
            button.style.color = 'white';

            // Reset after 2 seconds
            setTimeout(() => {
                button.textContent = originalText;
                button.style.backgroundColor = '';
                button.style.color = '';
            }, 2000);
        })
        .catch(err => {
            console.error('Failed to copy: ', err);
            button.textContent = 'Error!';
            button.style.backgroundColor = '#ef4444';
            button.style.color = 'white';

            // Reset after 2 seconds
            setTimeout(() => {
                button.textContent = 'Copy';
                button.style.backgroundColor = '';
                button.style.color = '';
            }, 2000);
        });
}

/**
 * Initializes smooth scrolling for navigation links
 */
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Update URL without reloading the page
                history.pushState(null, null, targetId);

                // Close mobile menu if open
                const navLinks = document.querySelector('.nav-links');
                if (navLinks && navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                    document.querySelector('.mobile-menu-btn')?.setAttribute('aria-expanded', false);
                }
            }
        });
    });
}

/**
 * Sets up the citation reference functionality
 */
function setupCitationReferences() {
    document.querySelectorAll('.citation-ref').forEach(citationRef => {
        citationRef.addEventListener('click', function(e) {
            e.preventDefault();

            const citationId = this.getAttribute('href');
            const citationElement = document.querySelector(citationId);

            if (citationElement) {
                // Highlight the citation
                citationElement.classList.add('highlight');

                // Scroll to it
                citationElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });

                // Remove highlight after a delay
                setTimeout(() => {
                    citationElement.classList.remove('highlight');
                }, 3000);
            }
        });
    });
}