<script>
    import Movie from "./lib/Movie/Movie.svelte";
    import User from "./lib/User/User.svelte";
    import Person from "./lib/Person/Person.svelte";
    import UserList from "./lib/User/UserList.svelte";
    let menu = 2;
</script>

<main class="container">
    <h2>Projeto Pycine</h2>

    <ul class="nav">
        <li>
            <a href="/" on:click|preventDefault={() => (menu = 1)}>Users</a>
            <ul>
                <li>
                    <a href="/" on:click|preventDefault={() => (menu = 11)}
                        >Create</a
                    >
                </li>
            </ul>
        </li>
        <li>
            <a href="/" on:click|preventDefault={() => (menu = 2)}>Movies</a>
        </li>
        <li>
            <a href="/" on:click|preventDefault={() => (menu = 3)}>Artist</a>
        </li>
    </ul>

    <div class="card">
        {#if menu === 1}
            <UserList />
        {:else if menu === 11}
            <User />
        {:else if menu === 2}
            <Movie />
        {:else if menu === 3}
            <Person />
        {:else}
            <p>invalid option</p>
        {/if}
    </div>
</main>

<style>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    ul li {
        display: inline-block;
        position: relative;
        background-color: black;
    }

    ul li a {
        display: block;
        padding: 10px 20px;
        color: rgb(12, 150, 0);
        text-decoration: none;
    }

    ul li ul {
        position: absolute;
        top: 100%;
        left: 0;
        z-index: 1;
        display: none;
    }

    ul li:hover ul {
        display: block;
    }
</style>
