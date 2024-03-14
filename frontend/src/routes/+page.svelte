<script lang="ts">
	import MainNavBar from '../components/MainNavBar.svelte';
	import FilesReport from '../components/home/FilesReport.svelte';
	import { onMount } from 'svelte';
	import type {Files} from '../backend/interfaces/files/files.js';
	import { getAllFiles } from '../backend/requests/file/get.ts';

	let files: Files

	onMount( async () => {
		files = await getAllFiles()
	})

</script>

<div class="main-content-home">
	<MainNavBar/>

	<FilesReport listOfFiles={files}/>
</div>

<style>
	.main-content-home {
			display: flex;
			flex-direction: row;
	}
</style>