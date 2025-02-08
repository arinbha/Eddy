"use client";
import { useState } from "react";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";

export const UploadButton = () => {
  const [calendar, setCalendar] = useState<File>();

  return (
    <div className="flex flex-col items-center justify-center gap-4">
      <Input
        className="center h-[400] w-[400] overflow-hidden whitespace-nowrap"
        type="file"
        onChange={(e) =>
          e.target.files ? setCalendar(e.target.files[0]) : null
        }
      />
      <Button type="submit">Upload Files</Button>
    </div>
  );
};
