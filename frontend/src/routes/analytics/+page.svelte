<script lang="ts">

import MainNavBar from '../../components/MainNavBar.svelte';
import FileNavBar from '../../components/analyics/FileNavBar.svelte';
import type { Files } from '../../backend/interfaces/files/files.js';
import { onMount } from 'svelte';
import { getAllFiles } from '../../backend/requests/file/get.js';

let files: Files

onMount( async () => {
	files = await getAllFiles()
})

</script>

<div class="main-content">
	<MainNavBar/>
	<FileNavBar files={files}/>
</div>

<style>
	.main-content {
			display: flex;
	}
</style>