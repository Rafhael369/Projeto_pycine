<script>
    let salvou = false;
    let id_if;
    let promise = getMovies();
    async function getMovies() {
        const res = await fetch(`http://localhost:8000/movies`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
    function handleClick() {
        promise = getMovies();
    }
    async function saveFavorite(id) {
        salvou = true;
        id_if = id;
        const res = await fetch(`http://localhost:8000/favorite/create`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ user_id: 1, movie_id: id }),
        });
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
</script>

<button on:click={handleClick}> list movies </button>

<!--
    get from endpoint /genres
    <select>
        <option>Drama</option>
    </select
-->

{#await promise}
    <p>...waiting</p>
{:then movies}
    <div class="table">
        {#each movies as m}
            {#if salvou && id_if == m.id}
                <p class="salve">Filme favoritado com sucesso!</p>
            {/if}
            <!-- svelte-ignore a11y-missing-attribute -->
            <p><img src={m.poster_path} /></p>
            <!-- <p>{m.id}</p> -->
            <p>{m.title}</p>
            <p>{m.genres}</p>
            <!-- TODO: salvar filme como favorito -->
            <button on:click={() => saveFavorite(m.id)}>Save</button>
        {/each}
    </div>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

<style>
    .table {
        margin-top: 20px;
        /* display: grid; */
        grid-template-columns: 1fr 1fr 1fr max-content;
        /* border: 1px solid #ccc; */
        padding: 10px;
    }
    .salve {
        color: green;
    }
</style>
