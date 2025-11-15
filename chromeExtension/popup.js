document.addEventListener('DOMContentLoaded', function() {
    const changeColorBtn = document.getElementById('changeColorBtn');
 
    
    changeColorBtn.addEventListener('click', async () => {
        // Get the current active tab

        let tabs = await chrome.tabs.query({ active: true, currentWindow: true });
        let tab = tabs[0];
		console.log(tab);
        // Execute a script in the context of the active tab
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: setPageBackgroundColor,
        });
    });
});
    
function setPageBackgroundColor() {
    let currentColor = document.body.style.backgroundColor;
    if (currentColor === 'white') {
        document.body.style.backgroundColor = '#f85454ff';
    }else {
        document.body.style.backgroundColor = 'white';
    }

    // let element = document.getElementsByClassName('KIOyzU')[0];;
    // element.innerText = "Yes!! You have reached the login Page..."
}