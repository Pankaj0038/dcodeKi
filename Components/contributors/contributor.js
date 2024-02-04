const contributor = document.getElementById('contributor');

let allContributorsGithub = [];

let allContributorsAvatar = [];

function fetchAllContributors() {

    fetch('https://api.github.com/repos/Pankaj0038/dcodeKi/contributors')
        .then(response => response.json())
        .then(data => {

            data.forEach(contributor => {
                let modified_avatar_url = contributor.avatar_url.replace('v=4', 's=64&v=4');
                allContributorsGithub.push(contributor.html_url);
                allContributorsAvatar.push(modified_avatar_url);
            });

            allContributorsGithub.forEach((githubLink, index) => {
                const contributorCard = document.createElement('div');
                contributorCard.classList.add('contributor-card');

                const avatar = document.createElement('img');
                avatar.src = allContributorsAvatar[index];

                const link = document.createElement('a');
                link.target = '_blank';
                link.href = githubLink;
                link.appendChild(avatar);

                contributorCard.appendChild(link);
                contributor.appendChild(contributorCard);
            });
        })
}
fetchAllContributors();
