import { useMemo } from 'react'

type Props = {
  files: File[]
  onChange: (files: File[]) => void
}

export function ImageUpload({ files, onChange }: Props) {
  const previews = useMemo(
    () => files.map((file) => ({ file, src: URL.createObjectURL(file) })),
    [files],
  )

  return (
    <div>
      <label>
        Upload evidence images
        <input
          type="file"
          accept="image/*"
          multiple
          onChange={(event) => onChange(Array.from(event.target.files || []))}
        />
      </label>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: '0.7rem' }}>
        {previews.map(({ file, src }, idx) => (
          <div key={file.name + idx}>
            <img src={src} className="thumb" alt={file.name} />
            <button type="button" onClick={() => onChange(files.filter((_, i) => i !== idx))}>
              Remove
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}
