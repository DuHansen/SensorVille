var header           = document.getElementById('header');
    var navigationHeader = document.getElementById('navigation_header');
    var content          = document.getElementById('content');
    var showSidebar      = false;

    function toggleSidebar()
    {
        showSidebar = !showSidebar;
        if(showSidebar)
        {
            navigationHeader.style.marginLeft = '-10vw';
            navigationHeader.style.animationName = 'showSidebar';
            content.style.filter = 'blur(2px)';
        }
        else
        {
            navigationHeader.style.marginLeft = '-100vw';
            navigationHeader.style.animationName = '';
            content.style.filter = '';
        }
    }

    function closeSidebar()
    {
        if(showSidebar)
        {
            showSidebar = true;
            toggleSidebar();
        }
    }
    document.addEventListener('DOMContentLoaded', (event) => {
    // Seu código JavaScript aqui
    window.addEventListener('resize', function(event) {
        if(window.innerWidth > 768 && showSidebar) 
        {  
            showSidebar = true;
            toggleSidebar();
        }
    });
});
    window.onload = function() {
    var divBoxes = document.querySelectorAll('.box');
    divBoxes.forEach(function(divBox) {
        document.addEventListener('DOMContentLoaded', (event) => {
        divBox.addEventListener('click', function() {
            window.location.href = this.getAttribute('onclick').split("'")[1];
        });
    });
});
};

document.getElementById('btnFormulario').addEventListener('click', () => {
    window.location.href = '/';
});

document.getElementById('btnPlanilha').addEventListener('click', () => {
    window.open('https://docs.google.com/spreadsheets/d/1-9IQzI47NFZH6sB22Q1taPclcu_6--uP8gI3fd4AHHI/edit?gid=0#gid=0', '_blank');
});

