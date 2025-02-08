"use client";
import { useState } from "react";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";
import { api } from "~/trpc/react";

export const UploadButton = () => {
  const [calendar, setCalendar] = useState("");
  const updateCalendar = api.calendar.import.useMutation();

  return (
    <div className="flex flex-col items-center justify-center gap-4">
      <Input
        className="center h-[400] w-[400] overflow-hidden whitespace-nowrap"
        type="file"
        onChange={async (e) => {
          const file = e.target.files?.item(0);

          if (!file) return;

          const string = await new Promise((resolve, reject) => {
            const reader = new FileReader();

            reader.onload = (event) => {
              resolve(event.target?.result);
            };

            reader.onerror = (error) => {
              reject(error);
            };

            reader.readAsText(file);
          });

          console.log(string as string);

          setCalendar(string as string);
        }}
      />
      <Button
        type="submit"
        onClick={() => updateCalendar.mutate({ file: calendar })}
      >
        Upload Files
      </Button>
    </div>
  );
};
