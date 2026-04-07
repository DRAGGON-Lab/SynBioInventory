import { useMemo } from "react";

type Props = {
  files: File[];
  onAdd: (files: File[]) => void;
  onRemove: (index: number) => void;
};

export function ImageUploader({ files, onAdd, onRemove }: Props) {
  const previews = useMemo(
    () => files.map((file) => ({ file, url: URL.createObjectURL(file) })),
    [files]
  );

  return (
    <section>
      <label className="field-label" htmlFor="image-upload">
        Evidence images
      </label>
      <input
        id="image-upload"
        type="file"
        accept="image/*"
        multiple
        onChange={(event) => {
          const fileList = event.target.files;
          if (!fileList) return;
          onAdd(Array.from(fileList));
          event.currentTarget.value = "";
        }}
      />
      <div className="image-grid">
        {previews.map(({ file, url }, index) => (
          <article key={`${file.name}-${index}`} className="image-item">
            <img src={url} alt={file.name} />
            <button type="button" onClick={() => onRemove(index)}>
              Remove
            </button>
          </article>
        ))}
      </div>
    </section>
  );
}
