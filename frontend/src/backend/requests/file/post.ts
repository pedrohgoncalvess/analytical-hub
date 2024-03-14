import { apiPath } from '../../main';
import axios from 'axios';
import type { DynamicRow } from '../../interfaces/files/row_preview.ts';

export async function tablePreview(file:object, separator:string, header:boolean) {

	const formData = new FormData();
	formData.append('file', file);
	const encodedSeparator = encodeURIComponent(separator);

	const response = await axios.post(`${apiPath}/file/preview?separator=${encodedSeparator}&header=${header}`, formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
	})

	return response.data as DynamicRow
}


export async function sendFile(file: object, separator:string, header:boolean) {

	const formData = new FormData();
	formData.append('file', file);
	const encodedSeparator = encodeURIComponent(separator);

	const response = await axios.post(`${apiPath}/file/upload?separator=${encodedSeparator}&header=${header}`, formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
	})

	return response.status
}