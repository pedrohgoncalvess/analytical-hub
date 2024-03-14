<script lang="ts">
	import type { Files, TableSchema } from '../../backend/interfaces/files/files.ts';
	import GraphArea from './GraphArea.svelte';
	import { getSchema } from '../../backend/requests/file/get.ts';
	import Charts from './Charts.svelte';
	export let files: Files | null = null
	let selectedFile: number | null = null
	let selectedSchema: TableSchema | null = null


	async function changeSelectedFile(id_file:number) {
		selectedFile = id_file
		selectedSchema = await getSchema(selectedFile)
	}
</script>
<Charts/>
<GraphArea fields={selectedSchema}/>

<div class="container-side-nav-bar">
	<h1 class="nav-title">Files</h1>
	<div class="side-nav-bar">
		{#if files}
			{#each files.files as file}
			<div class="item-nav-container">
				<div aria-hidden="true" on:click={() => changeSelectedFile(file.id)}>
					<i class:selected={selectedFile === file.id} class="fa-solid fa-file item-icon"></i><span class:selected={selectedFile === file.id} class="item-nav-desc">{`${file.name}.${file.type}`}</span>
				</div>
			</div>
			{/each}
		{/if}
	</div>
</div>
<style>

    .nav-title {
        font-size: 35px;
        text-align: center;
        margin: 3% 0 0 0;
        transition: 0.5s ease;
        color: white;
    }

    .container-side-nav-bar {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: auto;
        margin: 0;
        background-color: #b2b2b2;
        transition: 0.5s ease;
        border-radius: 3px;
    }

    .side-nav-bar {
        display: flex;
        flex-direction: column;
        margin: 10% 3% 0 5%;
    }

    .item-nav-container {
        margin: auto;
        border-radius: 6px;
        padding: 5%;
        text-align: center;
				font-size: 25px;
    }

    .item-nav-container:hover {
        background-color: #303e56;
				color: white;
    }

    .item-icon {
        font-size: 35px;
        align-self: center;
        color: white;
        transition: 0.5s ease;
        margin: 10% 0 0 0;
    }

		.selected {
        color: #303e56;
		}

    .item-nav-container:hover .selected {
        color: white;
    }


</style>