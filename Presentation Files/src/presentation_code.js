    // Function to update progress bar
    function updateBar() {
      const progress = (window.scrollY / totalHeight) * 100;
      progressBar.style.width = progress + '%';
    }
    // Function to update the total height when an expandable container is toggled
    function updateTotalHeight() {
      totalHeight = document.body.scrollHeight - window.innerHeight;
      updateBar();
    }

    // Function to run when the page is fully loaded
    window.onload = function () {
      // Update the total height once all elements are loaded
      updateTotalHeight();
    };

    // JavaScript function to toggle the visibility of an expandable container
    function toggleExpand(containerId) {
      const container = document.getElementById(containerId);
      container.classList.toggle('show');

      // Update the total height when an expandable container is toggled
      updateTotalHeight();
    }

    // function openExpandableContainer(url) {
    //   // Open a new popup window with the specified URL
    //   const popup = window.open(url, '_blank', 'width=1150, height=600');
    //   // Focus the new popup window
    //   if (popup) {
    //     popup.focus();
    //   }
    // }