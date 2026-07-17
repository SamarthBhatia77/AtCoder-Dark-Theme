// content.js

// Retrieve the stored theme preference (defaulting to dark mode)
chrome.storage.local.get(['theme'], (result) => {
  const theme = result.theme || 'dark';
  document.documentElement.setAttribute('data-atcoder-theme', theme);

  // Apply wrapper class to body as soon as it is available
  const applyBodyClass = () => {
    if (theme === 'dark') {
      document.body.classList.add('atcoder-dark');
    } else {
      document.body.classList.remove('atcoder-dark');
    }
  };

  if (document.body) {
    applyBodyClass();
  } else {
    const observer = new MutationObserver(() => {
      if (document.body) {
        applyBodyClass();
        observer.disconnect();
      }
    });
    observer.observe(document.documentElement, { childList: true });
  }
});

// Listen for real-time changes in storage to toggle the theme dynamically
chrome.storage.onChanged.addListener((changes, areaName) => {
  if (areaName === 'local' && changes.theme) {
    const newTheme = changes.theme.newValue;
    document.documentElement.setAttribute('data-atcoder-theme', newTheme);
    if (document.body) {
      if (newTheme === 'dark') {
        document.body.classList.add('atcoder-dark');
      } else {
        document.body.classList.remove('atcoder-dark');
      }
    }
  }
});
