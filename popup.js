// popup.js

document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('theme-toggle');
  const statusDesc = document.getElementById('status-desc');

  // Load the current preference from local storage (default to 'dark')
  chrome.storage.local.get(['theme'], (result) => {
    const isDark = (result.theme || 'dark') === 'dark';
    toggle.checked = isDark;
    updateStatusText(isDark);
  });

  // Handle toggle switches
  toggle.addEventListener('change', () => {
    const themeValue = toggle.checked ? 'dark' : 'light';
    chrome.storage.local.set({ theme: themeValue }, () => {
      updateStatusText(toggle.checked);
    });
  });

  function updateStatusText(isDark) {
    statusDesc.textContent = isDark ? 'Currently Enabled' : 'Currently Disabled';
  }
});
