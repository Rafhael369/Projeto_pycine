<script>
    let person_id = null;
    let person = null;
    let message = null;
    async function getPerson() {
        const res = await fetch(
            `http://localhost:8000/artist/name/${person_id}`
        );
        const data = await res.json();
        if (res.ok) {
            person = data;
            message = null;
        } else {
            person = null;
            message = `ID ${person_id} ${res.statusText}`;
        }
    }
</script>

<input
    bind:value={person_id}
    type="text"
    placeholder="Enter the actor's name"
/>
<button on:click={getPerson}> find </button>

<div class="table">
    {#if person !== null}
        <!-- <p>{person.id}</p> -->
        <img
            src="https://image.tmdb.org/t/p/w185{person.imagem}"
            alt="imagem do artista"
            width="100"
            height="100"
        />
        <p>{person.nome}</p>
        <p>{person.popularidade}</p>
    {:else if message !== null}
        <p class="error">{message}</p>
    {/if}
</div>

<style>
    .error {
        color: #e35a5a;
    }
    .table {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        /* border: 1px solid #ccc; */
        padding: 10px;
    }
</style>
