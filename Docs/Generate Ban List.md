<div align="center"><img src="../img/banner.jpg"></div>

<h1 align="center">Documentation for Setting Up Ban Lists</h1>

<p>This documentation provides an overview of the <code>ban_list_followers.txt</code> and <code>ban_list_following.txt</code> files used in the SubManager application for managing your GitHub interactions. These files are personal and must be created manually by the user in the root directory of the SubManager folder.</p>

<h2 align="center">Overview</h2>

<h3>ban_list_followers.txt</h3>
<ul>
    <li><strong>Purpose:</strong> This file contains a list of usernames of users who have followed you, but you do not wish to follow back.</li>
    <li><strong>Usage:</strong> By maintaining this list, you can manage your followers more effectively and avoid following users that you are not interested in.</li>
</ul>

<h3>ban_list_following.txt</h3>
<ul>
    <li><strong>Purpose:</strong> This file contains a list of usernames of users that you have followed, but you do not want to unfollow.</li>
    <li><strong>Usage:</strong> This allows you to keep track of users you wish to remain connected with, even if you decide to clean up your following list.</li>
</ul>

<h2 align="center">File Format</h2>

<p>Both files should be formatted as plain text files (<code>.txt</code>). Each username should be listed on a new line, as follows:</p>

<pre><code>username1
username2
username3
</code></pre>

<h2 align="center">Example Content</h2>

<h3>ban_list_followers.txt</h3>
<pre><code>user123
spam_account
unwanted_follower
</code></pre>

<h3>ban_list_following.txt</h3>
<pre><code>friend1
important_contact
favorite_artist
</code></pre>

<h2 align="center">Creating the Files</h2>
<h3 align="center">Windows</h3>

<h4>Using GUI</h4>
<ol>
    <li><strong>Navigate to the SubManager Directory:</strong>
        <p>Open File Explorer and go to the root directory of your SubManager folder.</p>
    </li>
    <li><strong>Create the Text Files:</strong>
        <ul>
            <li>Right-click in the directory.</li>
            <li>Select <strong>New</strong> and then choose <strong>Text Document</strong>.</li>
            <li>Name the file <code>ban_list_followers.txt</code> for the followers list.</li>
            <li>Create another file named <code>ban_list_following.txt</code> for the following list.</li>
        </ul>
    </li>
    <li><strong>Add Usernames:</strong>
        <p>Open each file in a text editor (such as Notepad) and enter the usernames you wish to ban, one per line.</p>
    </li>
</ol>

<h4>Using Command Line</h4>
<ol>
    <li><strong>Open Command Prompt:</strong>
        <p>Press <code>Windows + R</code>, type <code>cmd</code>, and press Enter.</p>
    </li>
    <li><strong>Navigate to the SubManager Directory:</strong>
        <pre><code>cd path\to\SubManager</code></pre>
    </li>
    <li><strong>Create the Text Files:</strong>
        <pre><code>echo. &gt; ban_list_followers.txt
echo. &gt; ban_list_following.txt</code></pre>
    </li>
    <li><strong>Add Usernames:</strong>
        <p>You can open the files in Notepad or any text editor to add usernames:</p>
        <pre><code>notepad ban_list_followers.txt
notepad ban_list_following.txt</code></pre>
    </li>
</ol>

<h3 align="center">Linux/MacOS</h3>
<h4>Using GUI</h4>
<ol>
    <li><strong>Navigate to the SubManager Directory:</strong>
        <p>Open Finder and go to the root directory of your SubManager folder.</p>
    </li>
    <li><strong>Create the Text Files:</strong>
        <ul>
            <li>Right-click in the directory (or use Control + Click).</li>
            <li>Select <strong>New Document</strong> or open TextEdit and create a new document.</li>
            <li>Save it as <code>ban_list_followers.txt</code> for the followers list.</li>
            <li>Create another file named <code>ban_list_following.txt</code> for the following list.</li>
        </ul>
    </li>
    <li><strong>Add Usernames:</strong>
        <p>Open each file in TextEdit and enter the usernames you wish to ban, one per line.</p>
    </li>
</ol>
<h4>Using Terminal</h3>
<ol>
    <li><strong>Open Terminal:</strong>
        <p>You can find Terminal in Applications &gt; Utilities or search for it using Spotlight (<code>Cmd + Space</code>). </p>
    </li>
    <li><strong>Navigate to the SubManager Directory:</strong>
        <pre><code>cd /path/to/SubManager</code></pre>
    </li>
    <li><strong>Create the Text Files:</strong>
        <pre><code>touch ban_list_followers.txt ban_list_following.txt</code></pre>
    </li>
    <li><strong>Add Usernames:</strong>
        <p>You can use a command-line text editor like nano or vim to edit the files:</p>
        <pre><code>nano ban_list_followers.txt
nano ban_list_following.txt</code></pre></p></li>

<h2 align="center">Important Notes</h2>
<ul>
    <li>Make sure there are no extra spaces or blank lines in the files, as this may impact how your GitHub interactions are managed by the SubManager application.</li>
    <li>These lists are personal; avoid sharing them with others to protect your privacy and maintain control over your social media connections.</li>
</ul>

<h2 align="center">Conclusion</h2>

<p>The <code>ban_list_followers.txt</code> and <code>ban_list_following.txt</code> files are crucial for effectively managing your interactions on GitHub through SubManager. By organizing your followers and following lists, you can enhance your experience and focus on meaningful connections.</p>