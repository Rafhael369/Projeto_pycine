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
    <table class="border-collapse border border-slate-400">
        <thead>
            <tr>
                <th class="border border-slate-300">id</th>
                <th class="border border-slate-300">name</th>
            </tr>
        </thead>
        <tbody>
            {#each movies as m}
                <tr>
                    <td class="border border-slate-300">{m.id}</td>
                    <td class="border border-slate-300">{m.name}</td>
                </tr>
            {/each}
        </tbody>
    </table>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

<style>
</style>
