<script>
    let promise = getMovies();
    async function getMovies() {
        const res = await fetch(`http://localhost:8000/favorite/movies/${1}`);
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
</script>

{#await promise}
    <p>...waiting</p>
{:then movies}
    <div class="table">
        {#each movies as m}
            <!-- svelte-ignore a11y-missing-attribute -->
            <p><img src={m.poster_path} /></p>
            <p>{m.name}</p>
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
</style>
